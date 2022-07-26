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


class Title(models.Model):
    """
    Section to update the page title 
    when necessary
    """

    class Meta:
        verbose_name_plural = 'Title Page'

    title_f = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.title_f
