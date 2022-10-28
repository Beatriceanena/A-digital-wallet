from rest_framework import serializers
from wallet.models import Customer,Wallet,Account,Card,Transaction,Loan,Reciept,Notification

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('first_name', 'email', 'age',)
 

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields=('currency','customer','date','balance',)
        
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('account_name','account_type','balance',)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields=('card_name','card_type','card_number','Account',)
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=('transaction_type','transaction_ID','transaction_charge',)        
      
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=('loan_amount','loan_type','loan_balance','loan_term',)
        
class RecieptSerializer(serializers.ModelField):
    class Meta:
        model=Reciept
        fields=('reciept_type', 'reciept_date','amount','account',)
        
class NotificationSerializer(serializers.ModelField):
    class Meta:
        model=Notification
        fields=('name','reciepient','time','date',)                     