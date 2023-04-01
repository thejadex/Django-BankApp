from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, DepositForm

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
    

""""
    Main Fuctions of the App. 
        When a user is not authenticated, they can't access these pages.  
        Hence, redirected to the login page - [@login_required]
"""    

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def deposit(request):
        
    if request.method == 'POST':
        if request.method == 'POST':
            form = DepositForm(request.POST)
            if form.is_valid():
                deposit = form.save(commit=False)
                deposit.user = request.user
                deposit.user_id = request.user.id
                deposit.first_name = request.user.first_name
                deposit.last_name = request.user.last_name
                deposit.username = request.user.username
                deposit.save()
            return redirect('dashboard')
    else:
        form = DepositForm()
    
    return render(request, 'deposit.html', {'form': form})

@login_required(login_url='login')
def withdraw(request):
    return render(request, 'withdraw.html')

@login_required(login_url='login')
def transfer(request):
    return render(request, 'transfer.html')
