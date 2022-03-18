from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'pls enter your username'}),
        label='username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'pls enter your password'}),
        label='password'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_username = User.objects.filter(username=username).exists()

        if not is_exists_username:
            raise forms.ValidationError('this is username not found or not register')
        else:
            return username


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'pls enter your username'}),
        label='username',
        validators=[validators.MinLengthValidator(5, 'pls enter must 5 character')]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'pls enter your password'}),
        label='password',
        validators=[validators.MinLengthValidator(8, 'pls enter must be 8 character')]
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'pls enter your config password'}),
        label='config password'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'pls enter your email'}),
        label='email',
        validators=[validators.EmailValidator('this is nor valid a email pls enter valid email')]
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_username = User.objects.filter(username=username).exists()

        if not is_exists_username:
            return username
        raise forms.ValidationError('this is took before username ')

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('passwords is not valid ')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_email = User.objects.filter(email=email).exists()

        if is_exists_email:
            raise forms.ValidationError('this email before took ')
        else:
            if '@gmail.com' not in email:
                if '@yahoo.com' not in email:
                    raise forms.ValidationError('pls enter valid email')
                else:
                    return email
            else:
                return email


class EditUserAccountForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'enter your first name', 'class': 'form-control'}
        ),
        label='first name'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'enter your last name', 'class': 'form-control'}
        ),
        label='last name'
    )
