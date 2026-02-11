from django.db import models
from apps.core.uploads import DataUpload
from apps.users.models import User

class UploadAuditLog(models.Model):
    data_upload = models.ForeignKey(DataUpload, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=100)
    performed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.action} on {self.data_upload.original_filename} by {self.performed_by.email}"
