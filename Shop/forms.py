from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm , PasswordResetForm , SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from . models import Customer



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



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))




class ChangePasswordFrom(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), widget = forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), widget = forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html()) 
    new_password2 = forms.CharField(label=_("New confrim Password"), widget = forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))


class PasswordResetForm(PasswordResetForm):
    email = forms.CharField(label=_('Email'), max_length=50, widget = forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}) )



class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), widget = forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html()) 
    new_password2 = forms.CharField(label=_("New confrim Password"), widget = forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','division','district','thana','villorroad','zipCode',]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}), 
            'division':forms.Select(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'thana':forms.TextInput(attrs={'class':'form-control'}),
            'villorroad':forms.TextInput(attrs={'class':'form-control'}),
            'zipCode':forms.NumberInput(attrs={'class':'form-control'}),     
            }