from rest_framework import serializers
from .models import User, UserProfile




class UserRegistrationSerializer(serializers.ModelSerializer):
    # profile=UserProfileSerializer()
    class Meta:
        model = User
        fields =  ['name','email','date_of_birth','phone_number','password','bloodgroup','province_number','address','issue']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def create(self, validated_data):
    #   profile_data = validated_data.pop('profile')
      user= User.objects.create_user(** validated_data)
    #   UserProfile.objects.create(user=user, **profile_data)
      return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    # userdetail=UserRegistrationSerializer(many=True)
    name = serializers.CharField(source='User.name', read_only=True)
    bloodgroup=serializers.CharField(source='User.bloodgroup',read_only=True)
    phone_number=serializers.CharField(source='User.phone_number',read_only=True)
    address=serializers.CharField(source='User.address',read_only=True)
    date_of_birth=serializers.CharField(source='User.date_of_birth',read_only=True)
    bloodgroup=serializers.CharField(source='User.bloodgroup',read_only=True)
    #userid=serializers.CharField(source='User.id',read_only=True)
    # bloodgroup=serializers.CharField(source='User.bloodgroup',read_only=True)
    class Meta:
        model=UserProfile
        fields=['profile_picture','name','bloodgroup','phone_number','address','date_of_birth']    
        # fields=['profile_picture']
    



class UserLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['phone_number', 'password']