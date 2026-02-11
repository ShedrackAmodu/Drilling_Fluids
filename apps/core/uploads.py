from django.db import models
from apps.users.models import User
from apps.core.models import Tenant

class DataUpload(models.Model):
    """Model to store metadata and raw files for uploads (Excel/CSV)"""
    UPLOAD_TYPE_CHOICES = [
        ('excel', 'Excel'),
        ('csv', 'CSV'),
    ]
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_type = models.CharField(max_length=10, choices=UPLOAD_TYPE_CHOICES)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    original_filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    error_report = models.TextField(blank=True)
    version = models.PositiveIntegerField(default=1)
    column_mapping = models.JSONField(blank=True, null=True)
    preview_data = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.original_filename} ({self.upload_type}) by {self.uploaded_by.email}"
