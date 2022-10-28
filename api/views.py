from urllib import response
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notification, Reciept, Transaction,Wallet
from .serializers import CustomerSerializer, WalletSerializer,AccountSerializer,CardSerializer,TransactionSerializer,LoanSerializer,RecieptSerializer,NotificationSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    

class WalletViewSet(viewsets.ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer
    
class AccountViewset(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
    
class AccountDepositView(viewsets.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)
    
class AccountTransferView(views.APIView):
    def post(self,request,pk,format=None):
        account_1=Account.objects.get(pk=pk)
        account_id=request.data["destination"]   
        amount=request.data["amount"]  
        try:
            account=Account.objects.get(id=account_id)   
        except ObjectDoesNotExist:  
            return Response("Account Not Found", status=404)
        message, status = account_1.transfer(account,amount)    
        return Response (message,status=status)
        

class AccountLoanRequestView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist: 
            return Response("Account Not Found", status=404)
        message, status = account.loan_request(amount) 
        return Response (message,status=status)


class AccountLoanRepaymentView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  
            return Response("Account Not Found", status=404)
        message, status = account.loan_repayment(amount) 
        return Response (message,status=status)


class AccountBuyAirtimeView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        airtime_money=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)

        except ObjectDoesNotExist:
            return Response("Account not found",status=404)

        message,status=account.buy_airtime(airtime_money)
        return Response(message,status=status)
  
    
class AccountWithdrawalView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        airtime_money=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)

        except ObjectDoesNotExist:
            return Response("Account not found",status=404)

        message,status=account.withdraw_money(account)
        return Response(message,status=status)    

    
class CardViewset(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    
class TransactionViewset(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    
class LoanViewset(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    
class RecieptViewset(viewsets.ModelViewSet):
    queryset=Reciept.objects.all()
    serializer_class=RecieptSerializer
    
class NotificationViewset(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer               
    
