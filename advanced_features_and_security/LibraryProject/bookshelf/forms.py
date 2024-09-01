from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book, CustomUser


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself'}), required=False)

class CustomUserCreationForm(UserCreationForm):
    ROLES = [

    ]