from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .import views


def Home(request):
    Products = Product.objects.all()
    return render(request, 'home.html', {'Products': Products})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            return redirect('Home')
        else:
            messages.error(
                request, "Incorrect username or password. Please try again.")
            return redirect('login_user')

    else:
        return render(request, 'login.html')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('Home')
        else:
            return redirect('register_user')
    else:
        return render(request, 'register.html', {'form': form})


def watches(request):
    Products = Product.objects.all()
    return render(request, 'watches.html', {'Products': Products})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})
