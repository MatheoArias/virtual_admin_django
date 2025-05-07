from django.contrib import admin
from .models import Maintenance


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "equipment",
        "liable",
        "number",
        "category",
        "date",
        "diagnostic",
        "activities")


admin.site.register(Maintenance, MaintenanceAdmin)
