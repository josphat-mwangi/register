from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    howmanyfollowerdoyouwant = forms.IntegerField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "howmanyfollowerdoyouwant"]