"""
model classes for access as admin
"""
from django.contrib import admin
from .models import Flavor, Title, History, Icon



class FlavorAdmin(admin.ModelAdmin):
    """
    models FlavorAdmin
    for description changes
    """
    list_display = (
        'description_f',
    )

admin.site.register(Flavor, FlavorAdmin)


class TitleAdmin(admin.ModelAdmin):
    """
    models TitleAdmin
    for description changes
    """
    list_display = (
        'title_f',
    )

admin.site.register(Title, TitleAdmin)


class HistoryAdmin(admin.ModelAdmin):
    """
    models HistoryAdmin
    for description changes
    """
    list_display = (
        'history_f',
    )

admin.site.register(History, HistoryAdmin)


class IconAdmin(admin.ModelAdmin):
    """
    models IconAdmin
    for icon changes
    """
    list_display = (
        'website',
    )

admin.site.register(Icon, IconAdmin)
