import random
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    account_balance = models.FloatField(default=0)
    account_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            # Generate a random account number
            while True:
                account_number = ''.join(random.choices('0123456789', k=10))
                if not UserAccount.objects.filter(account_number=account_number).exists():
                    break
            self.account_number = account_number
            self.username = self.user.username
        super().save(*args, **kwargs)

    def accountBalance_update(self, amount):
        self.accountBalance -= amount
        self.save()



class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    sender_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='sent_transaction')
    recipient_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='received_transaction')
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)


class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)