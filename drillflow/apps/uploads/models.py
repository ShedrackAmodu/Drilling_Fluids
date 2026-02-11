from django.db import models


class UploadedDataset(models.Model):
    tenant = models.ForeignKey('drillflow.apps.tenants.Tenant', on_delete=models.CASCADE)
    well = models.ForeignKey('drillflow.apps.wells.Well', on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='uploads/')
    version = models.CharField(max_length=50, default='v1')
    uploaded_by = models.ForeignKey('drillflow.apps.accounts.CustomUser', on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dataset {self.id} ({self.version})"
