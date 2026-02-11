from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import Tenant

class UserActionLog(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    extra_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.action} @ {self.timestamp}"
