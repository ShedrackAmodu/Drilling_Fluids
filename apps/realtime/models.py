from django.db import models
from apps.core.models import Tenant
from apps.users.models import User

class TimeSeries(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.tenant.name})"

class TimeSeriesPoint(models.Model):
    series = models.ForeignKey(TimeSeries, on_delete=models.CASCADE, related_name='points')
    timestamp = models.DateTimeField()
    value = models.FloatField()
    extra = models.JSONField(blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=['series','timestamp'])]

class IngestionJob(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=50)
    config = models.JSONField()
    last_run = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

class TenantUsage(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    metric = models.CharField(max_length=100)
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    limits = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

