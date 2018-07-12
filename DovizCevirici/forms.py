from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Sponsorlar

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,label='Adınız')
    last_name = forms.CharField(max_length=30, required=False,label='Soyadınız')
    email = forms.EmailField(max_length=254, help_text='Zorunlu. Lütfen E-Mail Adresinizi Doğru Giriniz.',label='E-Mail Adresiniz')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsorlar
        fields = ('sponsor_ad', 'sponsor_foto', )

class ContactForm(forms.Form):
    adiniz = forms.CharField(required=True,label='Adınız')
    soyadiniz = forms.CharField(required=True,label='Soyadınız')
    from_email = forms.EmailField(required=True,label='E-Posta Adresiniz:')
    subject = forms.CharField(required=True,label='Konu Nedir ?')
    message = forms.CharField(widget=forms.Textarea,label='Mesajınız:')


