
import random
from django.db import models
from django.contrib.auth.models import User

from .AES_encryption_whole import aes_combined

"""
    Note that these models are fields that are created in the database.
"""

class EncryptedField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is not None:
            return aes_combined(value)  # Decrypt the value
        return value

    def to_python(self, value):
        if value is not None:
            return aes_combined(value)  # Decrypt the value
        return value

    def get_prep_value(self, value):
        if value is not None:
            return aes_combined(value)  # Encrypt the value

# This Model creates a random account number for each user registered and their balance.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=30)
    username = EncryptedField(max_length=255)
    account_balance = models.FloatField(default=0)
    # account_number = models.CharField(max_length=10, unique=True)
    account_number = EncryptedField(max_length=255, unique=True)

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

    # @property
    # def decrypted_account_number(self):
    #     # Decrypt the account number and return the plaintext value
    #     decrypted = aes_combined(self.account_number)
    #     return decrypted

    # @property
    # def decrypted_username(self):
    #     # Decrypt the balance and return the plaintext value
    #     decrypted = aes_combined(self.username)
    #     return decrypted


# This model is used to allow users deposit into their accounts and their account balance is updated.
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=30)
    username = EncryptedField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

# Transfer between two accounts
class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='sent_transaction')
    # sender_username = models.CharField(max_length=30)
    sender_username = EncryptedField(max_length=255)
    receiver_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='received_transaction')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

# This model is used to allow users withdraw from their accounts and their account balance is updated.
class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=30)
    username = EncryptedField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)