from django.db import models
from apps.users.models import User

class Well(models.Model):
    """Well model for drilling operations"""
    name = models.CharField(max_length=100)
    api_number = models.CharField(max_length=50, unique=True)
    operator = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    depth_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    depth_measured = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wells_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.api_number})"

class WellSection(models.Model):
    """Well section model for different depth intervals"""
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=50)
    depth_start = models.DecimalField(max_digits=8, decimal_places=2)
    depth_end = models.DecimalField(max_digits=8, decimal_places=2)
    hole_size = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.well.name} - {self.name}"
