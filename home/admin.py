from django.contrib import admin
from .models import Flavor, Title



class FlavorAdmin(admin.ModelAdmin):
    list_display = (
        'description_f',
    )

admin.site.register(Flavor, FlavorAdmin)


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'title_f',
    )

admin.site.register(Title, TitleAdmin)
