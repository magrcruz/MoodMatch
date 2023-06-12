from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
# mypaymentapp/models.py
from decimal import *
from typing import Iterable

from payments import *
from payments.models import BasePayment
from payments import PaymentError, PaymentProvider
from mercadopago import MP

class MercadoPagoProvider(PaymentProvider):
    def get_gateway_url(self):
        return '/payments/process/'
   
    def get_token(self, request):
        # Obtén el token de acceso de Mercado Pago aquí usando tus credenciales de API
        return 'TU_TOKEN_DE_ACCESO'
   
    def process_payment(self, payment, request):
        mp = MP(self.get_token(request))
   
        # Crea una preferencia de pago en Mercado Pago y obtén el init_point
        preference = {
            "items": [{
                "title": payment.description,
                "quantity": 1,
                "currency_id": payment.currency,
                "unit_price": payment.total,
            }]
        }
   
        response = mp.create_preference(preference)
        init_point = response["response"]["init_point"]
   
        # Redirige al usuario a la página de pago de Mercado Pago
        return self.redirect(init_point)
   
    def process_data(self, payment, request):
        # Verifica el estado del pago y realiza cualquier acción adicional aquí
        mp = MP(self.get_token(request))
        payment_id = request.GET.get('payment_id')
   
        payment_info = mp.get_payment_info(payment_id)
        payment_status = payment_info['response']['status']
   
        if payment_status == 'approved':
            payment.change_status('confirmed')
        elif payment_status == 'pending':
            payment.change_status('waiting')
        elif payment_status == 'cancelled':
            payment.change_status('rejected')
        elif payment_status == 'refunded':
            payment.change_status('refunded')
   
        return self.redirect('/payments/success/')
