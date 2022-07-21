from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField



class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and orders
    """
    default_phone_number = models.CharField(max_length=10, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=32, null=True, blank=True)
    default_street_address = models.CharField(max_length=100, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)