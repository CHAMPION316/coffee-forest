""" Imports for default BagConfig class """
from django.apps import AppConfig


class BagConfig(AppConfig):
    """ default app.py class BagConfig """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
