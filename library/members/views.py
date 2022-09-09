import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, MemberForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('admin_welcome')
            else:
                return redirect('home')
        else:
           messages.warning(request,"Log in failed")
           return redirect("login")
    else:
         return render(request,'login.html')

def logout_member(request):
    logout(request)
    messages.success(request,"You were logged out")
    return redirect("login")

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        member_form = MemberForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user=user_form.save()
            member=member_form.save(commit=False)
            member.user=user
            member.save()
            messages.success(request, f'Your account was successfully created!')
            return redirect('login')

    else:
        user_form = UserForm()
        member_form = MemberForm()
    return render(request,'register.html', {'user_form': user_form,'member_form': member_form})
