from django.contrib import admin
from .models import Liable


class LiableAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'name', 'lastName', 'email', 'telephone','workstation')

 
admin.site.register(Liable, LiableAdmin)
