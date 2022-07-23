from django.contrib import admin
from .models import Flavor



class FlavorAdmin(admin.ModelAdmin):
    list_display = (
        'title_f',
        'description_f',
    )

admin.site.register(Flavor, FlavorAdmin)