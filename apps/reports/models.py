from django.db import models
from apps.users.models import User
from apps.core.models import Tenant

class ReportTemplate(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    template_json = models.JSONField(help_text='Template definition for report generation')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class ReportVersion(models.Model):
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE, related_name='versions')
    version = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    changelog = models.TextField(blank=True)

    class Meta:
        unique_together = ('template', 'version')

class GeneratedReport(models.Model):
    template = models.ForeignKey(ReportTemplate, on_delete=models.SET_NULL, null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parameters = models.JSONField()
    file = models.FileField(upload_to='reports/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Report {self.id} - {self.template.name if self.template else 'custom'}"
