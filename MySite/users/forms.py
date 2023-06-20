from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput,PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    username = CharField(max_length=200, required=True,widget=TextInput())
    password1 = CharField(max_length=200, required=True,widget=PasswordInput())
    password2 = CharField(max_length=200,required=True,widget=PasswordInput())

    class Meta:
        model = User
        fields = ("username","password1","password2")



class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']



















