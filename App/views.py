from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import messages
from decimal import Decimal

from .forms import CreateUserForm, DepositForm, TransferForm, WithdrawalForm
from .models import Transfer, UserAccount


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

    username = request.user.get_username()
    logout(request)
    messages.success(request, (f"Goodbye, {username}."))
    return redirect('login')

# Register User
def signup(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserAccount.objects.create(user=user) # Generates Account Number for each user
            username = request.user.get_username()
            login(request, user)
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
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.user_id = request.user.id
            deposit.first_name = request.user.first_name
            deposit.last_name = request.user.last_name
            deposit.username = request.user.username
            deposit.save()

            amount = float(request.POST.get('amount'))
            user_account = UserAccount.objects.get(user=request.user)
            user_account.account_balance += amount
            user_account.save()
            messages.success(request, f'Deposit of {amount} was successful!')
        return redirect('dashboard')
    else:
        form = DepositForm()
    
    return render(request, 'deposit.html', {'form': form})



@login_required(login_url='login')
def transfer(request):

    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
    else:
        form = TransferForm()


    return render(request, 'transfer.html', {'form': form})



@login_required(login_url='login')
def withdraw(request):

    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            withdraw = form.save(commit=False)
            withdraw.user = request.user
            withdraw.user_id = request.user.id
            withdraw.first_name = request.user.first_name
            withdraw.last_name = request.user.last_name
            withdraw.username = request.user.username
            withdraw.save()

            user_account = UserAccount
            user_account = UserAccount.objects.get(user=request.user)
            amount = float(request.POST.get('amount'))
            if amount <= user_account.account_balance:

                user_account.account_balance -= amount
                user_account.save()
                messages.success(request, f'Withdrawal of {amount} was successful!')

            elif amount > user_account.account_balance:
                messages.error(request, f'Withdrawal cannot be more than your account balance')
                messages.success(request, f'Withdrawal of {amount} was not successful!')
                
        return redirect('dashboard')
    else:
        form = WithdrawalForm()

    return render(request, 'withdraw.html',{"form": form})