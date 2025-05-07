from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "nit", "telephone", "address", "email", "city")


admin.site.register(Supplier, SupplierAdmin)
