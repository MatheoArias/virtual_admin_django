from django.contrib import admin
from .models import Equipment


class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'area',
        'name',
        'model',
        'code',
        'serie',
        'mannufacturer',
        'installed',
        'purchased',
        'description',
        'accesories',
        'manteinance_interval',
        'category',
        'image')


admin.site.register(Equipment, EquipmentAdmin)
