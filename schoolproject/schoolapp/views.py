from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def home(requests):
    return render(requests, 'index.html')


def login(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(requests, user)
            return render(requests,'welcome.html')
        else:
            messages.info(requests, "Invalid credentials")
            return redirect('login')
    return render(requests, 'login.html')


def register(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']
        password2 = requests.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(requests, "Username already exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(requests, "Password does not match")
            return redirect('register')
        return redirect('/')
    return render(requests, 'register.html')


def welcome(requests):
    return render(requests, 'welcome.html')


def form(requests):
    if requests.method=='POST':

        messages.info(requests, "Order Confirmed")
        return redirect('form')
    return render(requests, 'form.html')
