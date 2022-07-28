from django.contrib import admin
from .models import Flavor, Title, History, Icon



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


class HistoryAdmin(admin.ModelAdmin):
    list_display = (
        'history_f',
    )

admin.site.register(History, HistoryAdmin)


class IconAdmin(admin.ModelAdmin):
    list_display = (
        'website',
    )

admin.site.register(Icon, IconAdmin)