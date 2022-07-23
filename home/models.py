from django.db import models


class Flavor(models.Model):
    """
    A section that is updated with current
    flavors and information
    """

    class Meta:
        verbose_name_plural = 'Flavors'

    title_f = models.CharField(max_length=30, null="True", blank="True")
    description_f = models.TextField()

    def __str__(self):
        return self.title_

    def __str__(self):
        return self.description_f