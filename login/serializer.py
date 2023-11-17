from rest_framework import serializers
from login.models import RegistrationModel

class RegisterSerailizer(serializers.ModelSerializer):
    class Meta:
        model=RegistrationModel
        fields=(
             'name',
             'image',
             'email',
             'password',
             
              
    
        )