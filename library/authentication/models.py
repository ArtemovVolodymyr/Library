from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authentication.enums.role import RoleEnum
from authentication.manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    middle_name = models.CharField(max_length=20, default=None)
    email = models.CharField(max_length=100, unique=True, default=None)
    password = models.CharField(default=None, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.IntegerField(choices=RoleEnum.choices)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'

    def __repr__(self):
        return f"{CustomUser.__name__}(id={self.id})"
