from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class LoginForm(forms.Form):
     username = forms.CharField(
        max_length=150,
        label="Username",
        required=True
    )
     password= forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        required=True
    )