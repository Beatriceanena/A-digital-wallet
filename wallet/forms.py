from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Account, Card, Customer, Loan, Notification, Reciept, Reward, Thirdparty, Transaction, Wallet


class CustomerRegistrationForm(forms.ModelForm):
      class Meta:
          model=Customer
          fields="__all__"
class AccountRegistrationForm(forms.ModelForm):
     class Meta:
          model=Account
          fields="__all__"

class WalletRegistrationForm(forms.ModelForm):
     class Meta:
          model=Wallet
          fields="__all__"       

class TransactionRegistrationForm(forms.ModelForm):
     class Meta:
          model=Transaction
          fields="__all__"             

class CardRegistrationForm(forms.ModelForm):
     class Meta:
          model=Card
          fields="__all__"

class NotificationRegistrationForm(forms.ModelForm):
     class Meta:
          model=Notification
          fields="__all__"

class ThirdpartyRegistrationForm(forms.ModelForm):
     class Meta:
          model=Thirdparty
          fields="__all__"

class RecieptRegistrationForm(forms.ModelForm):
     class Meta:
          model=Reciept
          fields="__all__"

class LoanRegistrationForm(forms.ModelForm):
     class Meta:
          model=Loan
          fields="__all__"

class RewardRegistrationForm(forms.ModelForm):
     class Meta:
          model=Reward
          fields="__all__"                  