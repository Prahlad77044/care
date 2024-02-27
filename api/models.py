from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save

#custom user model
class UserManager(BaseUserManager):
    def create_user(self, name, email, date_of_birth, phone_number, bloodgroup, province_number, address, issue, password=None):
        """
        Creates and saves a User with the given  name, email, date_of_birth,phone_number, bloodgroup, province_number, address, issue,
        """
        if not phone_number:
            raise ValueError("Users must have an Phone Number")

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            bloodgroup=bloodgroup,
            province_number=province_number,
            address=address,
            issue=issue,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, date_of_birth, phone_number, bloodgroup, province_number, address, issue, password=None):
        """
        Creates and saves a superuser with the given name, email, date_of_birth, phone_number,
        bloodgroup, province_number, address, issue,and password.
        """

        user = self.create_user(
            name=name,
            email=self.normalize_email(email),
            password=password,
            date_of_birth=date_of_birth,
            phone_number=phone_number, 
            bloodgroup=bloodgroup,
            province_number=province_number,
            address=address,
            issue=issue,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        # Create a profile instance for superuser
        # UserProfile.objects.create(user=user)
        return user



class User(AbstractBaseUser):
    
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(verbose_name="phone number",max_length=15,unique=True,)
    bloodgroup = models.CharField(max_length=5)
    province_number = models.IntegerField()
    address = models.CharField(max_length=200)
    issue = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
   
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'email', 'date_of_birth','bloodgroup','province_number','address','issue']  
    

    def __str__(self):
      return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def has_perms(self, perm_list, obj=None):
        """
        Return True if the user has each of the specified permissions. If object is
        passed, check if the user has all required perms for it.
        """
        # Check if the user has all the permissions in perm_list
        return all(self.has_perm(perm, obj) for perm in perm_list)
    



#---------------------------------------------------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)    
    

def create_user_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)


def _save_user_profile(sender,instance,**kwargs):
    instance.userprofile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(_save_user_profile,sender=User)