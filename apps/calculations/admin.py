from django.contrib import admin
from .models import Calculation, Workflow, CalculationUnit

@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    """Admin interface for Calculation model"""
    list_display = ('name', 'calculation_type', 'well', 'created_by', 'created_at')
    list_filter = ('calculation_type', 'well__name', 'created_at')
    search_fields = ('name', 'well__name')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    """Admin interface for Workflow model"""
    list_display = ('name', 'description', 'created_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CalculationUnit)
class CalculationUnitAdmin(admin.ModelAdmin):
    """Admin interface for CalculationUnit model"""
    list_display = ('name', 'symbol', 'is_default')
    search_fields = ('name', 'symbol')
    list_filter = ('is_default',)
    ordering = ('name',)
