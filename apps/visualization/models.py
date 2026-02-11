from django.db import models
from apps.users.models import User
from apps.core.models import Tenant

class Dashboard(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    layout = models.JSONField(help_text='Layout and widgets configuration')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_shared = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.tenant.name})"

class ChartWidget(models.Model):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='widgets')
    title = models.CharField(max_length=150)
    widget_type = models.CharField(max_length=50, choices=[('rheology','Rheology'),('depth','Depth'),('time_series','Time Series')])
    query = models.JSONField(help_text='Query/config for generating the chart')
    options = models.JSONField(blank=True, null=True)
    position = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.widget_type}"
