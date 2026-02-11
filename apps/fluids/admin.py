from django.contrib import admin
from .models import FluidType, FluidProperty, FluidSample, FluidMeasurement

@admin.register(FluidType)
class FluidTypeAdmin(admin.ModelAdmin):
    """Admin interface for FluidType model"""
    list_display = ('name', 'abbreviation', 'description')
    search_fields = ('name', 'abbreviation')

@admin.register(FluidProperty)
class FluidPropertyAdmin(admin.ModelAdmin):
    """Admin interface for FluidProperty model"""
    list_display = ('name', 'unit', 'description')
    search_fields = ('name', 'unit')

@admin.register(FluidSample)
class FluidSampleAdmin(admin.ModelAdmin):
    """Admin interface for FluidSample model"""
    list_display = ('sample_name', 'well', 'fluid_type', 'depth', 'temperature', 'created_by', 'created_at')
    list_filter = ('fluid_type', 'well__name', 'created_at')
    search_fields = ('sample_name', 'well__name')
    readonly_fields = ('created_at',)

@admin.register(FluidMeasurement)
class FluidMeasurementAdmin(admin.ModelAdmin):
    """Admin interface for FluidMeasurement model"""
    list_display = ('fluid_sample', 'property', 'value', 'temperature', 'measured_at')
    list_filter = ('property__name', 'fluid_sample__sample_name', 'measured_at')
    search_fields = ('fluid_sample__sample_name', 'property__name')
    readonly_fields = ('measured_at',)
