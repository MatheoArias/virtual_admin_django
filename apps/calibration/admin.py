from django.contrib import admin
from .models import Calibration


class CalibrationAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'supplier',
                    'number',
                    'date',
                    'calibration_range_max',
                    'calibration_range_min',
                    'uncertainty',
                    'error',
                    'file')


admin.site.register(Calibration, CalibrationAdmin)
