from django import forms
from django.contrib.auth.models import User


# NOTE: Форма регистрации с хабра
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
