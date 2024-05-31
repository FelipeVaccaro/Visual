from django.urls import path
from .views import init_transaction, transaction_return

urlpatterns = [
    path('transaction/init/', init_transaction, name='init_transaction'),
    path('transaction/return/', transaction_return, name='transaction_return'),
]