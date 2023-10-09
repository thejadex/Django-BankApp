
import random
from django.db import models
from django.contrib.auth.models import User


"""
    Note that these models are fields that are created in the database.
"""

# This Model creates a random account number for each user registered and their balance.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    account_balance = models.FloatField(default=0)
    account_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            # Generates a random account number
            while True:
                account_number = ''.join(random.choices('0123456789', k=10))
                if not UserAccount.objects.filter(account_number=account_number).exists():
                    break
            self.account_number = account_number
            self.username = self.user.username
        super().save(*args, **kwargs)

    def accountBalance_update(self, amount):
        self.account_balance -= amount
        self.save()



# This model is used to allow users deposit into their accounts and their account balance is updated.
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

# Transfer between two accounts
class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='sent_transaction')
    sender_username = models.CharField(max_length=255)
    receiver_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='received_transaction')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

# This model is used to allow users withdraw from their accounts and their account balance is updated.
class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)