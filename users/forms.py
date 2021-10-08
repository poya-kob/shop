from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "نام کاربری"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': " رمز عبور"}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': "رمز عبور"}))
    password2 = forms.CharField(label='repeat_password',
                                widget=forms.PasswordInput(attrs={'placeholder': " تکرار رمز عبور"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام'
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'phone')
