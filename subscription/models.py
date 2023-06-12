from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
# mypaymentapp/models.py
from decimal import *
from typing import Iterable

from payments import PurchasedItem
from payments.models import BasePayment

class Payment(BasePayment):

    def get_failure_url(self) -> str:
        # Return a URL where users are redirected after
        # they fail to complete a payment:
        return redirect(reverse("moodMatch:genre_preferences"))
    def get_success_url(self) -> str:
        # Return a URL where users are redirected after
        # they successfully complete a payment:
        return redirect(reverse("moodMatch:genre_preferences"))

    def get_purchased_items(self) -> Iterable[PurchasedItem]:
        # Return items that will be included in this payment.
        yield PurchasedItem(
            name='The Hound of the Baskervilles',
            sku='BSKV',
            quantity=9,
            price=Decimal(10),
            currency='USD',
        )