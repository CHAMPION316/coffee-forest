from django.db import models


class Category(models.Model):
    name = models.Charfield(max_length=254)
    frinedly_name = models.Charfield(max_length=254, null=True, blank=True)