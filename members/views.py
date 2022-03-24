from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

from carwash.models import Carwash

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There Was An Error Logging In, Please Try Again'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You Were Logged Out!'))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            
            # create User Carwash Profile
            user_profile = Carwash(carwash_purchased=0, free_code=0, main_user=request.user)
            user_profile.save()

            messages.success(request, ('Registration Successful!'))
            return redirect('home')
    else:
        form = RegisterUserForm()    

    return render(request, 'authenticate/register_user.html', {
        'form': form
    })

