from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=300,required=True,widget=forms.TextInput())

    password1 = forms.CharField(max_length=399,required=True,widget=forms.TextInput())
    password2 = forms.CharField(max_length=399,required=True,widget=forms.TextInput())
    
    class Meta:
        model = User
        fields = ["username","password1","password2"]



    


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]