from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    website = forms.CharField(widget=forms.CharField, max_length=30, label='Website')
    phonenumber = forms.IntegerField(widget=forms.IntegerField, max_value=9999999999999999,label='Phonenumber')
    class Meta:
        model=User
        fields=['username','email','password','website']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['username','password']



