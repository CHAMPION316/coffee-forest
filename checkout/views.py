from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currenty=settings.STRIPE_CURRENCY,
    )
    
    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LJmKuC7HW1slj1MR56rpzn6hn2pKpCl4w5R3xRkdwL2p44bCcBlooLBk5YwVqGGIOReGmRAwJfiywlkh7enx4Jz00ju7O4ayL',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)