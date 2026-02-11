from django.contrib import admin
from .models import ReportTemplate, ReportVersion, GeneratedReport

@admin.register(ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'tenant', 'created_by', 'created_at')
    search_fields = ('name', 'tenant__name')

@admin.register(ReportVersion)
class ReportVersionAdmin(admin.ModelAdmin):
    list_display = ('template', 'version', 'created_at')
    search_fields = ('template__name',)

@admin.register(GeneratedReport)
class GeneratedReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'template', 'tenant', 'generated_by', 'status', 'created_at')
    list_filter = ('status', 'tenant')
