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
    def update(self,
            first_name=None,
            last_name=None,
            middle_name=None,
            password=None,
            role=None,
            is_active=None):
        user_to_update = CustomUser.objects.filter(email=self.email).first()
        if first_name != None and len(first_name) <= 20:
            user_to_update.first_name = first_name
        if last_name != None and len(last_name) <= 20:
            user_to_update.last_name = last_name
        if middle_name != None and len(middle_name) <= 20:
            user_to_update.middle_name = middle_name
        if password != None:
            user_to_update.password = password
        if role != None:
            user_to_update.role = role
        if is_active != None:
            user_to_update.is_active = is_active
        user_to_update.save()