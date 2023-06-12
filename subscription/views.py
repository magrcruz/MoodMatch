# mypaymentapp/views.py
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from django.shortcuts import render, redirect
from payments.models import Payment

def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return TemplateResponse(
        request,
        'subscription/subscription.html',
        {'form': form, 'payment': payment}
    )



def process_payment(request):
    # Crea una instancia de Payment y guárdala en tu base de datos
    payment = Payment.objects.create(
        total=100,  # Total a pagar
        currency='ARS',  # Moneda
        description='Descripción del pago',  # Descripción
        status='pending',  # Estado inicial
    )
   
    # Procesa el pago
    payment.process(request)
   
    return redirect(payment.get_success_url())

def payment_success(request):
    return render(request, 'subscription/payment_success.html')
