from django.urls import path
from .views import *

app_name = 'subscription'

urlpatterns = [
    path('payment_details/<payment_id>', payment_details, name='payment_details'),
]