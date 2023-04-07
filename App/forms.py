from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deposit, Transfer, Withdraw, UserAccount


class CreateUserForm(UserCreationForm):

    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User

        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2',
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
        }


class DepositForm(forms.ModelForm):

    class Meta:
        model = Deposit
        fields = ['amount']



class TransferForm(forms.Form):

    receiver_account = forms.CharField(max_length=10, label='Beneficiary Account')
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    
    def clean_recipient_account_number(self):
        account_number = self.cleaned_data['receiver_accountNumber']
        try:
            UserAccount.objects.get(account_number=account_number)
        except UserAccount.DoesNotExist:
            raise forms.ValidationError("Account with that number does not exist.")
        return account_number
    

class WithdrawalForm(forms.ModelForm):

    class Meta:
        model = Withdraw
        fields = ['amount']