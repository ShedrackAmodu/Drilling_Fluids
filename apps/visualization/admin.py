from django.contrib import admin
from .models import Dashboard, ChartWidget

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'tenant', 'created_by', 'is_shared', 'created_at')
    search_fields = ('name', 'tenant__name', 'created_by__email')
    list_filter = ('is_shared', 'tenant')
    ordering = ('-created_at',)

@admin.register(ChartWidget)
class ChartWidgetAdmin(admin.ModelAdmin):
    list_display = ('title', 'dashboard', 'widget_type')
    search_fields = ('title', 'dashboard__name')
