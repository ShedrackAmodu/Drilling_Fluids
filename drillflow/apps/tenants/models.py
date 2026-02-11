from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    subscription_plan = models.CharField(max_length=100, blank=True)
    settings = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
