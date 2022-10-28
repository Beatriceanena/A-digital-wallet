from atexit import register
from django.urls  import path,include

from wallet.models import Notification
from .views import account_profile, card_profile, customer_profile, edit_account, edit_card, edit_profile, edit_reciept, edit_transaction, edit_wallet, list_account, list_card, list_customer, list_loan, list_notification, list_reciept, list_reward, list_thirdparty, list_transaction, list_wallet, reciept_profile, register_customer,register_account,register_notification,register_reciept,register_loan,register_reward,register_wallet,register_transaction,register_card,register_thirdparty, transaction_profile, wallet_profile

from django.contrib import admin

urlpatterns =[ 
    path("register/",register_customer,name="registration"),
    path("account/",register_account,name="account"),
    path("notification/",register_notification,name="notification"),
    path("reciept/",register_reciept,name="reciept"),
    path("loan/",register_loan,name="loan"),
    path("wallet/",register_wallet,name="wallet"),
    path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("reward/",register_reward,name="reward"),
    path("customers/",list_customer,name="customer"),
    path("accounts/",list_account,name="account"),
    path("notifications/",list_notification,name="notification"),
    path("reciepts/",list_reciept,name="reciept"),
    path("loans/",list_loan,name="loan"),
    path("wallets/",list_wallet,name="wallet"),
    path("transactions/",list_transaction,name="transaction"),
    path("cards/",list_card,name="card"),
    path("thirdpartys/",list_thirdparty,name="thirdparty"),
    path("rewards/",list_reward,name="reward"),
    path("customers/<int:id>/",customer_profile, name="customer_profile"),
    path("customers/edit/<int:id>/",edit_profile,name="edit_profile"),
    path("wallets/<int:id>/",wallet_profile, name="wallet_profile"),
    path("wallets/edit/<int:id>/",edit_wallet,name="edit_wallet"),
    path("accounts/<int:id>/",account_profile, name="account_profile"),
    path("accounts/edit/<int:id>/",edit_account,name="edit_account"),
    path("cards/<int:id>/",card_profile, name="card_profile"),
    path("cards/edit/<int:id>/",edit_card,name="edit_card"),
    path("transactions/<int:id>/",transaction_profile, name="transaction_profile"),
    path("transactions/edit/<int:id>/",edit_transaction,name="edit_transaction"),
    path("reciepts/<int:id>/",reciept_profile, name="reciept_profile"),
    path("reciepts/edit/<int:id>/",edit_reciept,name="edit_reciept")
]


   

