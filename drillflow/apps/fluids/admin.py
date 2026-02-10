from django.contrib import admin
from .models import FluidSystem


@admin.register(FluidSystem)
class FluidSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'tenant', 'well', 'density')
    list_filter = ('type',)
