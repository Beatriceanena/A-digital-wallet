from django.contrib import admin
from .models import Customer, Wallet, Account, Transaction, Card, Thirdparty, Notification,Reciept, Loan, Reward

class customerAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","nationality","email", "address")
    search_fields=("firstname","lastname",)
admin.site.register(Customer,customerAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display=("currency","customer","balance")
    search_fields=("customer","balance")
admin.site.register(Wallet,WalletAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","account_type","wallet","balance")
    search_fields=("account_name", "account_number","wallet")
admin.site.register(Account,AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_Amount","wallet", "transaction_date", "transaction_charge","destination_account")
    search_fields=("transaction_Amount","transcation_date","transaction_charge")
admin.site.register(Transaction,TransactionAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=("card_name","card_type","wallet","Account")
    search_fields=("card_name", "card_type","wallet")
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=("name","Account","phonenumber")
    search_fields=("name","Account")
admin.site.register(Thirdparty,ThirdpartyAdmin)


class NotificationAdmin(admin.ModelAdmin):
      list_display=("name","recipient","time","date")
      search_fields=("name","reciepient")
admin.site.register(Notification,NotificationAdmin)


class RecieptAdmin(admin.ModelAdmin):
    list_display=("reciept_type", "amount","account_number","transaction","reciept_date")
    search_fields=("reciept_type","account_number")
admin.site.register(Reciept,RecieptAdmin)
   
class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_amount","loan_type","loan_balance","loan_term","due_date")
    search_fields=("loan_amount","loan_type","loan_balance")   
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("date","customerId","transaction","reward_points")
    search_fields=("date","reward_points")
admin.site.register(Reward,RewardAdmin)

# Register your models here.

