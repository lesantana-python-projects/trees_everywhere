from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Account


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class LoginForm(forms.Form):
    username = forms.CharField(label='User')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    account = forms.ModelChoiceField(Account.objects.filter(active=True).all())
