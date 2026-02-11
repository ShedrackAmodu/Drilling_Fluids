from django.contrib import admin
from .upload_audit import UploadAuditLog

@admin.register(UploadAuditLog)
class UploadAuditLogAdmin(admin.ModelAdmin):
    list_display = ('data_upload', 'action', 'performed_by', 'timestamp')
    search_fields = ('data_upload__original_filename', 'performed_by__email', 'action')
    list_filter = ('action',)
    ordering = ('-timestamp',)
