from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Organization

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Organization
        fields = ('__all__')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Organization
        fields = ('__all__')