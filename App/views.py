from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

def homepage(request):
    return render(request, 'layout.html')

# Authenticate Login Request
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
    
# Authenticate Logout Request
def logoutUser(request):

    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('login')


def signup(request):

    form = CreateUserForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()

    return render(request, 'signup.html', {'form':form})
    

def dashboard(request):
    return render(request, 'dashboard.html')


def deposit(request):
    return render(request, 'deposit.html')


def withdraw(request):
    return render(request, 'withdraw.html')


def transfer(request):
    return render(request, 'transfer.html')
