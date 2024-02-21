from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['name','email','date_of_birth','phone_number','password','bloodgroup','province_number','address','issue']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def create(self, validated_data):
        return User.objects.create_user(** validated_data)
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['phone_number', 'password']