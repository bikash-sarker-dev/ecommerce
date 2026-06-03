from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs={'class':'form-control mb-4'}))
    email = forms.CharField(required=True, widget= forms.EmailInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        labels ={'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}