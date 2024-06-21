from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    username      = models.CharField(unique=True, max_length=20)
    email         = models.EmailField()
    password      = models.CharField(max_length=20)
    rol           = models.CharField(max_length=20)
    departamento  = models.CharField(max_length=20)
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD    = 'email'
    def __str__(self):
        return "Usuario: " + str(self.username)