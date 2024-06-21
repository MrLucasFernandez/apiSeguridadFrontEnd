from rest_framework import serializers
from api.models import Usuario

"""
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.hashers import make_password
"""
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'departamento', 'rol')
        EMAIL_FIELD = 'username'
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Usuario(**validated_data)
        user.set_password(password)
        
        user.save()
        return user