from django.db import models


class Flavor(models.Model):
    """
    A section that is updated with current
    flavors and information
    """

    class Meta:
        verbose_name_plural = 'Flavors'

    description_f = models.TextField()

    def __str__(self):
        return self.description_f
