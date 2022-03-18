from django import forms
from django.core import validators


class ContactUs(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'pls enter your full name', 'class': 'form-control'}),
        label='fullname',
        validators=[validators.MinLengthValidator(5, 'pls enter be must 5 character')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'pls enter your email', 'class': 'form-control'}),
        label='Email',
        validators=[validators.EmailValidator('pls enter valid email')]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'pls enter your subject', 'class': 'form-control'}),
        label='subject',
        validators=[validators.MinLengthValidator(5, 'pls enter be must 5 character')]
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'pls enter your text', 'class': 'form-control'}),
        label='text',
        validators=[validators.MinLengthValidator(10, 'pls enter be must 10 character')]
    )