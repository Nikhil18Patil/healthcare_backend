from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid

class CustomUserManager(BaseUserManager):
    """Custom user manager to create users using email instead of username"""

    def create_user(self, email, first_name, last_name, mobile, password=None):
        if not email:
            raise ValueError("Email is required")
        if not mobile:
            raise ValueError("Mobile number is required")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, mobile, password=None):
        user = self.create_user(email, first_name, last_name, mobile, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model using email instead of username"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "mobile"]

    def __str__(self):
        return self.email

