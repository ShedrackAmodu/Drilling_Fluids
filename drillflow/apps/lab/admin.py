from django.contrib import admin
from .models import RheologyTest


@admin.register(RheologyTest)
class RheologyTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'fluid_system', 'recorded_at', 'temperature')
    search_fields = ('fluid_system__id',)
