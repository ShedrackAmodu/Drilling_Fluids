from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('ENGINEER', 'Engineer'),
        ('CLIENT', 'Client'),
        ('VIEWER', 'Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ENGINEER')
    tenant = models.ForeignKey('drillflow.apps.tenants.Tenant', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.get_full_name() or self.username
