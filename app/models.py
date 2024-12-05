from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
class UserProfileManager(BaseUserManager):
    def create_user(self,email,fn,ln,password=None):
        if not email:
            raise ValueError('Email feild is mandratory')
        email = self.normalize_email(email)
        User = self.model(email=email,First_name = fn,Last_name = ln)
        User.set_password(password)
        User.save()
        return User
    def create_superuser(self,email,First_name,Last_name,password):
        user_object = self.create_user(email,First_name,Last_name,password)
        user_object.set_password(password)
        user_object.is_superuser = True
        user_object.is_staff = True
        user_object.save()

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=100,primary_key=True)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['First_name','Last_name']
