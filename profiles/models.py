"""
User profile fields for admin and UI
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField



class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and orders
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=50, null=True, blank=True)
    default_street_address = models.CharField(max_length=100, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=100, null=True, blank=True)
    default_county = models.CharField(max_length=100, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)


    # Existing users: just save the profile
    def save_profile(sender, instance, **kwargs):
        instance.userprofile.save()
