from django.urls import path, include
from rest_framework import routers

from .views import CustomerViewSet,WalletViewSet,AccountViewset,CardViewset,TransactionViewset,LoanViewset,RecieptViewset,NotificationViewset,AccountDepositView,AccountTransferView,AccountWithdrawalView,AccountLoanRequestView,AccountLoanRepaymentView,AccountBuyAirtimeView

router= routers.DefaultRouter()
router.register("customers", CustomerViewSet)
router.register("wallets", WalletViewSet)
router.register("accounts", AccountViewset)
router.register("cards", CardViewset)
router.register("transactions", TransactionViewset)
router.register("loans", LoanViewset)
router.register("reciepts", RecieptViewset)
router.register("notifications", NotificationViewset)
router.register("deposit", AccountDepositView)
router.register("transfer", AccountTransferView)
router.register("transfer", AccountWithdrawalView)
router.register("transfer", AccountLoanRequestView)
router.register("transfer", AccountLoanRepaymentView)
router.register("transfer", AccountBuyAirtimeView)


urlpatterns = [
    path ("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"), 
    path("transfer/<int:pk>/", AccountTransferView.as_view(), name="transfer-view"),
    path("withdrawal/", AccountWithdrawalView.as_view(),name="withrawal-view"),
    path("loan_request/",AccountLoanRequestView.as_view(),name="loan-view"),
    path("loan_repayment/",AccountLoanRepaymentView.as_view(),name="repay-loan-view"),
    path("buy_airtime/",AccountBuyAirtimeView.as_view(),name="repay-loan-view")
]

