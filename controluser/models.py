from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class User(AbstractBaseUser):

    objects = UserManager()
    login = models.CharField(max_length=30,default="None", unique=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=120)
    tipoAcesso = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login

    @property
    def is_admin(self):
        return self.admin

class UserManager(BaseUserManager):
    def criar_usuario(self, login=None, password=None):

        if not login:
            raise ValueError('Usuários devem possuir um login')

        user = self.model(login, password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def criar_admin(self, login, password):

        user = self.criar_usuario(login, password=password,)
        user.tipoAcesso = True
        user.save(using=self._db)
        return user

