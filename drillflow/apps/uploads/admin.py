from django.contrib import admin
from .models import UploadedDataset


@admin.register(UploadedDataset)
class UploadedDatasetAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'version', 'tenant', 'uploaded_by', 'uploaded_at')
    list_filter = ('version', 'tenant')
