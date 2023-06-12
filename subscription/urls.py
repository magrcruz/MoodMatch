from django.urls import path
from .views import process_payment, payment_success, payment_details

app_name = 'subscription'

urlpatterns = [
    path('payment_details/<payment_id>', payment_details, name='payment_details'),
    path('payments/process/', process_payment, name='payment_process'),
    path('payments/success/', payment_success, name='payment_success'),
]