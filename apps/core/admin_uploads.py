from django.contrib import admin
from .uploads import DataUpload

@admin.register(DataUpload)
class DataUploadAdmin(admin.ModelAdmin):
    list_display = ('original_filename', 'upload_type', 'tenant', 'uploaded_by', 'uploaded_at', 'status', 'version')
    search_fields = ('original_filename', 'uploaded_by__email', 'tenant__name')
    list_filter = ('upload_type', 'status', 'tenant')
    ordering = ('-uploaded_at',)
