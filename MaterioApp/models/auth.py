from typing import Any, Optional
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

def user_type(key):
    return {
        "ombor":1,
        "magazin":3,
        "derector":1
    }.get(key,0)



class CustomUserManager(UserManager):
    def create_user(self, phone, password=None, is_staff=False, is_superuser=False, is_active=True, **extra_fields):
        user = self.model(phone=phone, password=password,
                          is_staff=is_staff, is_superuser=is_superuser, is_active=is_active, **extra_fields)
        user.set_password(password)
        user.save()     
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        return self.create_user(phone=phone, password=password, is_staff=True, is_superuser=True, is_active=True,
                                **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=128)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    type = models.SmallIntegerField(default=0)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def format(self):
        return {
            "name":self.name,
            "phone":self.phone,
            "type":self.type
        }
