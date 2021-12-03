from django import forms

from .models import AccRequest
from ..accounts.models import User, Profile


class account_request_form(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': " Residents First Name"
            }
        ))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Resident's Last Name"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enter An Active Email Address"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }
        )
    )

    class meta:
        model = AccRequest
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


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
