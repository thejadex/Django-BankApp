from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request, 'layout.html')


def loginUser(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
            # Redirect to a successful login page
        else:
            messages.success(request, ("There was an error logging in, try again!"))
            return redirect('login')
                    
    else:
        return render(request, 'login.html')


def logoutUser(request):

    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('login')

def signup(request):
    return render(request, 'signup.html')


def deposit(request):
    return render(request, 'deposit.html')


def withdraw(request):
    return render(request, 'withdraw.html')


def transfer(request):
    return render(request, 'transfer.html')
