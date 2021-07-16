from django.shortcuts import render
from abhikash_app.models import student
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from abhikash_app.forms import UserForm,UserFormStudent
# Create your views here.

def create_user(request):
    form1=UserForm()
    form2=UserFormStudent()
    if request.method=='POST':
        form1=UserForm(request.POST)
        form2=UserFormStudent(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user2=form2.save()
            user.refresh_from_db()
            user2.refresh_from_db()
            username=form1.cleaned_data.get('username')
            password=form1.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user2.save()
            print("username :"+form1.cleaned_data['username'])
            user=authenticate(username=username,password=password)
            login(request,user)
            return render(request,"abhikash_app/create_student.html",{'form1':form1,'form2':form2})
    return render(request,"abhikash_app/create_student.html",{'form1':form1,'form2':form2})
