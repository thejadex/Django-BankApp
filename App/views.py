from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.

def homepage(request):
    return render(request, 'layout.html')

# Authenticate Login Request
def loginUser(request):
    
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
                
		if user is not None:
			login(request, user)
			return redirect('dashboard')
                
		else:
			messages.success(request, ("Invalid Username or Password"))	
			return redirect('login')	
                
	else:
		return render(request, 'login.html')

        
                    
    
# Authenticate Logout Request
def logoutUser(request):

    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('login')


def signup(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request, 'signup.html', {'form': form})
    

def dashboard(request):
    return render(request, 'dashboard.html')


def deposit(request):
    return render(request, 'deposit.html')


def withdraw(request):
    return render(request, 'withdraw.html')


def transfer(request):
    return render(request, 'transfer.html')
