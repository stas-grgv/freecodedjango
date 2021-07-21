from django import forms
from django.contrib.auth.models import User


# NOTE: Форма регистрации с хабра
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=16)
