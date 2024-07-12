from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import UserContact
from django.forms import ModelForm
class CreateUserForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'repassword', 'photo']
class CreateContactForm(ModelForm):
    class Meta:
        model = UserContact
        fields = ['username', 'email', 'address']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)