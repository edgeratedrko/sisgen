from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    login = forms.CharField(max_length=30)
    nome = forms.CharField(max_length=100)
    cargo = forms.CharField(max_length=120)
    tipoAcesso = forms.BooleanField()

    class Meta:
        model = User
        fields = ['login', 'nome', 'password', 'password2', 'cargo', 'tipoAcesso']