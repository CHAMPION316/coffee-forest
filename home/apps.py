"""
apps.py standard django config
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    class HomeConfig default django
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
