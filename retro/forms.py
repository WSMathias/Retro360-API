from django import forms
from django.contrib.auth.models import User
from retro.models import RetroUser


class RetroUserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = RetroUser
        fields = '__all__'

class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = '__all__'

