from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['login', 'nome', 'password', 'password2', 'cargo', 'ADM']