from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    
    class Meta:
        model= User
        fields= [ 'username', 'email', 'password1', 'password2']
        
# class UserLoginForm(forms.Form):
    # username= forms.CharField(max_length=100)
    # password= forms.CharField(widget=forms.PasswordInput)