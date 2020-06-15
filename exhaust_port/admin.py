from django.contrib import admin
from exhaust_port.models import XWing, DefenceTower


class XWingAdmin(admin.ModelAdmin):
    list_display = ('name', 'pilot', 'health')


class DefenceTowerAdmin(admin.ModelAdmin):
    list_display = ('target', 'health')


admin.site.register(DefenceTower, DefenceTowerAdmin)
admin.site.register(XWing, XWingAdmin)
