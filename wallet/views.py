from django.shortcuts import render,redirect
from wallet.models import Account, Card, Customer, Loan, Notification, Reciept, Reward, Thirdparty, Transaction, Wallet
from .forms import CustomerRegistrationForm,CardRegistrationForm,AccountRegistrationForm,NotificationRegistrationForm,RecieptRegistrationForm,LoanRegistrationForm,WalletRegistrationForm,TransactionRegistrationForm, ThirdpartyRegistrationForm,RewardRegistrationForm


#Customer

def register_customer(request):
     if request.method == "POST":
         form = CustomerRegistrationForm(request.POST)
         if  form.is_valid():
             form.save()    
     else:
        form = CustomerRegistrationForm()
     return render (request,'wallet/register_customer.html',{ "form" : form})

def list_customer(request):
    customers =Customer.objects.all()
    return render(request,'wallet/customer_list.html',{"customers":customers})


def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",
                  {"customer":customer})
    
def edit_profile(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect("customer_profile", id=customer.id)
    else:
        form=CustomerRegistrationForm(instance=customer)
    return render(request,"wallet/edit_profile.html",
                      {"form":form})      


#Account

def register_account(request):
     if request.method == "POST":
         form = AccountRegistrationForm(request.POST)
         if  form.is_valid():
             form.save()
     else:
         form=AccountRegistrationForm()
     return render (request,'wallet/register_account.html',{ "form" : form})


def list_account(request):
    accounts =Account.objects.all()
    return render(request,'wallet/account_list.html',{"accounts":accounts})

def account_profile(request,id):
    account=Account.objects.get(id=id)
    return render(request,"wallet/account_profile.html",
                  {"account":account})
    
def edit_account(request,id):
    account=Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
        return redirect("account_profile", id=account.id)
    else:
        form=AccountRegistrationForm(instance=account)
        return render(request,"wallet/edit_account.html",
                      {"form":form})  


#Notification

def register_notification(request):
     if request.method == "POST":
         form=NotificationRegistrationForm(request.POST)
         if  form.is_valid():
             form.save()  
     else:
         form=NotificationRegistrationForm()    
     return render(request,"wallet/register_notification.html",{"form":form})
 
def list_notification(request):
     notifications =Notification.objects.all()
     return render(request,'wallet/notification_list.html',{"notifications":notifications})





#Reciept
def register_reciept(request):
     if request.method == "POST":
         form=RecieptRegistrationForm(request.POST)
         if  form.is_valid():
             form.save()   
     else:
         form=RecieptRegistrationForm()
     return render(request,"wallet/register_reciept.html",{"form":form})
 
  
def list_reciept(request):
     reciept = Reciept.objects.all()
     return render(request,'wallet/reciept_list.html',{"reciept":reciept})
 
def reciept_profile(request,id):
    reciept=Reciept.objects.get(id=id)
    return render(request,"wallet/reciept_profile.html",
                  {"reciept":reciept})
    
def edit_reciept(request,id):
    reciept=Reciept.objects.get(id=id)
    if request.method=="POST":
        form=RecieptRegistrationForm(request.POST, instance=reciept)
        if form.is_valid():
            form.save()
        return redirect("reciept_profile", id=reciept.id)
    else:
        form=RecieptRegistrationForm(instance=reciept)
        return render(request,"wallet/edit_reciept.html",
                      {"form":form})  



#Loan
def register_loan(request):
     if request.method == "POST":
         form=LoanRegistrationForm(request.POST)
         if  form.is_valid():
             form.save()         
     else:
         form=LoanRegistrationForm
     return render(request,"wallet/register_loan.html",{"form":form})
 
def list_loan(request):
     loans =Loan.objects.all()
     return render(request,'wallet/loan_list.html',{"loans":loans})



#Card
def register_card(request):
     if request.method == "POST":
         form=CardRegistrationForm(request.POST)
         if  form.is_valid():
             form.save() 
     else: 
         form=CardRegistrationForm     
     return render(request,"wallet/register_card.html",{"form":form})
 
def list_card(request):
     cards =Card.objects.all()
     return render(request,'wallet/card_list.html',{"cards":cards})
 

def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request,"wallet/card_profile.html",
                  {"card":card})
    
def edit_card(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
        return redirect("card_profile", id=card.id)
    else:
        form=CardRegistrationForm(instance=card)
        return render(request,"wallet/edit_card.html",
                      {"form":form})      


#Wallet
def register_wallet(request):
     if request.method == "POST":
         form=WalletRegistrationForm(request.POST)
         if  form.is_valid():
             form.save() 
     else:
         form=WalletRegistrationForm    
     return render(request,"wallet/register_wallet.html",{"form":form})
 
def list_wallet(request):
    wallets =Wallet.objects.all()
    return render(request,'wallet/wallet_list.html',{"wallets" : wallets})
 
def wallet_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    return render(request,"wallet/wallet_profile.html",
                  {"wallet":wallet})
    
def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("edit_wallet", id=wallet.id)
    else:
        form=WalletRegistrationForm(instance=wallet)
    return render(request,"wallet/edit_wallet.html",
                      {"form":form})  


#Transaction
def register_transaction(request):
     if request.method == "POST":
         form=TransactionRegistrationForm(request.POST)
         if  form.is_valid():
             form.save() 
     else:  
         form=TransactionRegistrationForm
     return render(request,"wallet/register_transaction.html", {"form":form})
 
def list_transaction(request):
    transactions =Transaction.objects.all()
    return render(request,'wallet/transaction_list.html',{"transactions" : transactions})

def transaction_profile(request,id):
    transcation=Transaction.objects.get(id=id)
    return render(request,"wallet/transaction_profile.html",
                  {"transaction":transcation})
    
def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
        return redirect("transaction_profile", id=transaction.id)
    else:
        form=TransactionRegistrationForm(instance=transaction)
        return render(request,"wallet/edit_transaction.html",
                      {"form":form})      


#Thirdparty

def register_thirdparty(request):
     if request.method == "POST":
         form=ThirdpartyRegistrationForm()
         if  form.is_valid():
             form.save()  
     else:
         form=ThirdpartyRegistrationForm    
     return render(request,"wallet/register_thirdparty.html",{"form":form})
 
def list_thirdparty(request):
    thirdpartys =Thirdparty.objects.all()
    return render(request,'wallet/thirdparty_list.html',{"thirdpartys" : thirdpartys})

#Reward

def register_reward(request):
     if request.method == "POST":
         form=RewardRegistrationForm(request.POST)
         if  form.is_valid():
             form.save()  
     else: 
         form=RewardRegistrationForm  
     return render(request,"wallet/register_reward.html", {"form":form})
 
def list_reward(request):
    rewards =Reward.objects.all()
    return render(request,'wallet/reward_list.html',{"rewards" : rewards})
 
 


# Create your views here.
