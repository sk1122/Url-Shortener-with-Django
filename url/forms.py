from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Url(forms.Form):
    url = forms.CharField(label="URL")


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }
