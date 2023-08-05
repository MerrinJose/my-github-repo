from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def register(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        firstname = requests.POST['firstname']
        lastname = requests.POST['lastname']
        email = requests.POST['email']
        password1 = requests.POST['password1']
        password_confirm = requests.POST['password2']
        if password1 == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.info(requests, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(requests, "email id already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname,
                                            last_name=lastname, password=password1, email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(requests, "Password does not match")
            return redirect('register')
        return redirect('/')
    return render(requests, 'register.html')

            #         if User.objects.filter(username=username).exists():
    #             messages.info(requests, "Username already exists")
    #             return redirect('register')
    #         elif User.objects.filter(email=email).exists():
    #             messages.info(requests, "email id already exists")
    #             return redirect('register')
    #         else:


    #             return redirect('login')
    #     else:
    #         messages.info(requests, "Password does not match")
    #         return redirect('register')
    #     return redirect('/')

def login(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password1 = requests.POST['password1']
        user = auth.authenticate(username=username, password=password1)

        if user is not None:
            auth.login(requests, user)
            return redirect('/')
        else:
            messages.info(requests, "Invalid credentials")
            return redirect('login')
    return render(requests, 'login.html')


def logout(requests):
    auth.logout(requests)
    return redirect('/')
