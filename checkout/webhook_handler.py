from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean data in the shipping_details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        order = Order.objects.get(
            full_name__iexact=shipping_details.name,
            email__iexact=shipping_details.email,
            phone_number__iexact=shipping_details.phone,
            country__iexact=shipping_details.country,
            postcode__iexact=shipping_details.postal_code,
            town_or_city__iexact=shipping_details.city,
            street_address__iexact=shipping_details.line1,
            county__iexact=shipping_details.state,
            grand_total=grand_total,
        )
        order_exists = True

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)