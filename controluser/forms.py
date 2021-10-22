from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    login = forms.CharField(max_length=30)
    nome = forms.CharField(max_length=100)
    cargo = forms.CharField(max_length=120)
    tipoAcesso = forms.BooleanField()

    class Meta:
        model = User
        fields = ['login', 'nome', 'senha', 'senha2', 'cargo', 'tipoAcesso']