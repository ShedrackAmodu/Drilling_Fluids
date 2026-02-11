from django.contrib import admin
from .models import Well, WellSection

@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    """Admin interface for Well model"""
    list_display = ('name', 'api_number', 'operator', 'field', 'location', 'depth_total', 'created_by', 'created_at')
    list_filter = ('operator', 'field', 'created_at')
    search_fields = ('name', 'api_number', 'operator', 'field')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

@admin.register(WellSection)
class WellSectionAdmin(admin.ModelAdmin):
    """Admin interface for WellSection model"""
    list_display = ('well', 'name', 'depth_start', 'depth_end', 'hole_size', 'created_at')
    list_filter = ('well__name', 'created_at')
    search_fields = ('well__name', 'name')
    readonly_fields = ('created_at',)
