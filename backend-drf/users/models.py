from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#three things to keep in mind when we want to extend the user model in django
#AbstractUser, AbstractBaseUser, and BaseUserManager


class User(AbstractUser):
    email = models.EmailField (unique=True)
    
    USERNAME_FIELD = 'email' #by default it is username but we are changing it to email
    REQUIRED_FIELDS = ['username'] #by default django need username if we dont wnat this we will use abstractBaseUser instead of abstractUser but we will use this for now and we will make username as required field
    
    def __str__(self):
        return self.email
    