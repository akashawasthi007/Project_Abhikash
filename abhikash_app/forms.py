from django import forms
from django.contrib.auth.models import User
from abhikash_app.models import student


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserFormStudent(forms.ModelForm):
    class Meta():
        model = student
        fields = ('name','branch','year','sec','mob_no')
