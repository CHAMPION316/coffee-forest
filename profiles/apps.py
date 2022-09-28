"""
apps.py django default config
for profiles app
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    ProfilesConfg default class for
    profiles app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
