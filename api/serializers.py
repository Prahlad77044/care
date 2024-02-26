from rest_framework import serializers
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    #userdetail=UserRegistrationSerializer(many=True,read_only=True)
    class Meta:
        model=UserProfile
        fields='__all__'

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
    




    
    
class UserLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['phone_number', 'password']