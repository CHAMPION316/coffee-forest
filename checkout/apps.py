"""checkout config for checkout"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    checkout class default
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
