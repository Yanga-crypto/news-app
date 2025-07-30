from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[
        ("reader", 'Reader'),
        ("editor", 'Editor'),
        ("journalist", 'Journalist')
    ])

    # Look into adding publisher field

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'user_type']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["publisher"]