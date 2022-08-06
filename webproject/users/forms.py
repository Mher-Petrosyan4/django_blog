from django import forms
from django.contrib.auth.models import User

from helpers.choices import GenderChoice
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileModelForm(forms.ModelForm):
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GenderChoice.choices, required=True)

    class Meta:
        model = Profile
        fields = ["profile_image", "bio", "age", "gender"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]