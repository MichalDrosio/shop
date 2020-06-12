from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from account.models import ProfileUser
from account.validators import number_selphone, check_postal_code


class LoginForm(forms.Form):
    username = forms.CharField(label='Użytkownik')
    password = forms.CharField(label='Hasło' ,widget=forms.PasswordInput)



class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Nick')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)



    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')


class UserProfileForm(forms.ModelForm):
    nr_selfphone = forms.CharField(validators=[number_selphone])
    postal_code = forms.CharField(validators=[check_postal_code])

    class Meta:
        model = ProfileUser
        exclude = ['user']



