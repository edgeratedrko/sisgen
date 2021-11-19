from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):

    def create_user(self, login=None, password=None):
        if not login:
            raise ValueError('Usuários devem possuir um login')

        user = self.model(
            login=login,
            password=password
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, login=None, password=None):
        user = self.create_user(
            login=login,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    login = models.CharField(max_length=30,default="", unique=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=120)
    ADM = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login

    def save(self, *args, **kwargs):
        if "is_crypted" not in self.__dict__:
            self.password = make_password(self.password)
            self.is_crypted = True
        elif not self.is_crypted:
            self.password = make_password(self.password)
            self.is_crypted = True
        
        super(User, self).save(*args, **kwargs)

    """
    @property
    def is_admin(self):
        return self.admin
    """
#

