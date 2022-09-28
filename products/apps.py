"""
default config for django
"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    default apps,py products config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
