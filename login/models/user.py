from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    username = models.CharField(max_length=25, null=True)
    identification = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)

    fcm_token = models.CharField(max_length=255, null=True, blank=True)
    fcm_tokens = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'identification'
    REQUIRED_FIELDS = ['username', 'password']

