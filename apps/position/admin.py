from django.contrib import admin
from .models import Position


class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name")


admin.site.register(Position, PositionAdmin)
