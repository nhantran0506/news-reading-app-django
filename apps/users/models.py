from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from apps.roles.enums import Roles

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    # password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    role = models.CharField(choices=Roles.choices(), max_length=15)

    reset_code = models.CharField(max_length=6, blank=True, null=True)
    reset_code_expiry = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'users'
        abstract = False
