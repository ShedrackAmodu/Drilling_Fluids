from django.contrib import admin
from .standards_audit import StandardsAuditLog

@admin.register(StandardsAuditLog)
class StandardsAuditLogAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'user', 'action', 'timestamp')
    search_fields = ('tenant__name', 'user__email', 'action')
    list_filter = ('action', 'tenant')
    ordering = ('-timestamp',)
