from django import forms
from django.contrib.auth.models import User
from .models import Member
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'John'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Doe'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'john.doe'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'john@doe.com'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'********'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'********'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class MemberForm(forms.ModelForm):
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'03000000'}))
    birthdaydate=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control my-2','placeholder':'MM-DD-YYYY'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Saida'}))
    class Meta:
        model = Member
        fields = ('phone', 'birthdaydate', 'address')
