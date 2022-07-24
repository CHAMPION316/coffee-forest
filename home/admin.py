from django.contrib import admin
from .models import Flavor



class FlavorAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

admin.site.register(Flavor, FlavorAdmin)