PAYMENT_VARIANTS = {
    # ...
    'MercadoPago':('payments_mercadopago.MercadoPagoProvider',{
        'access_token': 'MERCADO_PAGO_SANDBOX_ACCESS_TOKEN',
        'sandbox_mode': True})
}

CHECKOUT_PAYMENT_CHOICES = [('MercadoPago', 'Mercado Pago')]