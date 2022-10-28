from django.db import models
from email.headerregistry import Address
from django.utils import timezone


# Create your models here.

class Customer(models.Model):
     first_name=models.CharField(max_length=15,null=True)
     last_name=models.CharField(max_length=15,null=True)
     email=models.EmailField(max_length=25,null=True)
     nationality=models.CharField(max_length=15, null=True)
     age=models.CharField(max_length=10, null=True)
     phonenumber=models.CharField(max_length=15,null=True)
     gender=models.CharField(max_length=10, null=True)
     address=models.CharField(max_length=15,null=True)
     profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    

class Wallet(models.Model): 
     currency=models.CharField(max_length=15,null=True)
     customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='Wallet_Customer')
     date=models.DateTimeField(default=timezone.now)
     balance=models.IntegerField()
     pin=models.TextField(max_length=4, null=True)

class Account(models.Model):
     account_name=models.CharField(max_length=15, null=True)
     account_type=models.CharField(max_length=15,null=True )
     account_number=models.CharField(max_length=15, null=True)
     balance=models.IntegerField()
     wallet=models.ForeignKey('wallet', on_delete=models.CASCADE, related_name='Account_wallet')
     
     
# Deposit method
   
def deposit(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.account_balance += amount
           self.save()
           message = f"You have deposited {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status
 
  
#Transfer method
  
def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.account_balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.account_balance -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status
  



class Transaction(models.Model):
     wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name="Transaction_Wallet" )
     transaction_Amount= models.IntegerField()   
     transaction_date=models.DateTimeField(default=timezone.now)
     transcation_ID=models.CharField(max_length=10, null=True)
     transaction_type=models.CharField(max_length=15, null=True)
     transaction_charge=models.IntegerField()
     #reciept=models.ForeignKey('Reciept', on_delete=models.CASCADE, related_name='Transaction_Reciept')
     transaction_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_transaction_account')
     destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')
    
class Card(models.Model):
     card_name=models.CharField(max_length=15, null=True)
     card_type=models.CharField(max_length=15,null=True)
     card_number=models.IntegerField()
     wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name='Card_Wallet' )
     Account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Card_Account')

class Thirdparty(models.Model):
     name=models.CharField(max_length=15, null=True)
     Account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Thirdparty_Account')
     phonenumber= models.CharField(max_length=15, null=True)

class Notification(models.Model):
     name=models.CharField(max_length=15, null=True)
     recipient=models.CharField(max_length=15, null=True)
     time=models.DateTimeField(default=timezone.now)
     date=models.DateTimeField(default=timezone.now)

class Reciept(models.Model):
     reciept_type=models.CharField(max_length=20, null=True)
     amount=models.IntegerField()
     account_number=models.IntegerField(default=0)
     transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='Reciept_Transcation')
     reciept_date=models.DateTimeField(default=timezone.now)

class Loan(models.Model):
     loan_amount=models.IntegerField()
     loan_type=models.CharField(max_length=15, null=True)
     loan_balance=models.CharField(max_length=15, null=True)
     wallet=models.ForeignKey('wallet', on_delete=models.CASCADE, related_name='Loan_wallet')
     date=models.DateTimeField(default=timezone.now)
     gauranter=models.CharField(max_length=15, null=True)
     loan_term=models.IntegerField()
     due_date=models.DateTimeField(default=timezone.now)

class Reward(models.Model):
     date=models.DateTimeField(default=timezone.now)
     customerId=models.CharField(max_length=8, null=True)
     transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='Transaction_Reward')
     reward_points=models.CharField(max_length=15, null=True)

# Create your models here.
