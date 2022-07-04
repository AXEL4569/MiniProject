from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib import messages

# Create your views here.

def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or password")
            return redirect('sign-in')
    else:
        return render(request, 'sign_in.html', {})

def signOut(request):
    logout(request)
    return redirect('home')

def signUp(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Sign up Successful, One last step to set up your profile')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('sign-up')
    else:
        form = forms.SignUpForm()
        return render(request, 'sign_up.html', {'form': form, })

