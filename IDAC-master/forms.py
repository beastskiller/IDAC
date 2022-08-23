from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from IDACapp1.models import Contact


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class  ContactForm(ModelForm):
    class Meta:
      
        model =  Contact
        fields = ['email','subject','msg']