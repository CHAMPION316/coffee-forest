from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LJmKuC7HW1slj1MR56rpzn6hn2pKpCl4w5R3xRkdwL2p44bCcBlooLBk5YwVqGGIOReGmRAwJfiywlkh7enx4Jz00ju7O4ayL',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)