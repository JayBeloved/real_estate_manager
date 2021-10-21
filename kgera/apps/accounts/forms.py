from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import User, Profile

ADMIN = 1
SEC = 2
BASIC = 3

USERTYPE_CHOICES = (
    (ADMIN, 'Administrator'),
    (SEC, 'Secretary'),
    (BASIC, 'Basic User'),
)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "input100"
            }
        ))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input100"
            }
        ))


class ProfileInfoForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "readonly": True
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "readonly": True
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "readonly": True
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "readonly": True
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileInfoUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfilePicsUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
