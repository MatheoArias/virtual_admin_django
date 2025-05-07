from django.contrib import admin
from .models import MeasuringEquipment


class MeasuringEquipmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "equipment",
        "meassurment_range_max",
        "meassurment_range_min",
        "resolution",
        "emp",
        "magnitude"
    )


admin.site.register(MeasuringEquipment, MeasuringEquipmentAdmin)
