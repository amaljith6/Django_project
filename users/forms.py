from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Enter your E-mail ID ')

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField(label='Enter your E-mail ID ')

    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    # email = forms.EmailField(label='Enter your E-mail ID ')

    class Meta:
        model=Profile
        fields=['image']