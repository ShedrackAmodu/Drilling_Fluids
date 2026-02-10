from django.contrib import admin
from .models import CalculationRun


@admin.register(CalculationRun)
class CalculationRunAdmin(admin.ModelAdmin):
    list_display = ('id', 'calculation_type', 'tenant', 'well', 'created_at')
    list_filter = ('calculation_type', 'tenant')
