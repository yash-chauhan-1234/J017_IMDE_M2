from email.policy import default
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import toDo
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "first_name", "last_name", "password1", "password2"]

class toDoForm(forms.ModelForm):
    class Meta:
        model=toDo
        
        fields="__all__"