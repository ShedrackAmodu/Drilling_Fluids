from django.db import models
from apps.users.models import User
from apps.wells.models import Well

class FluidType(models.Model):
    """Fluid type model (WBM, OBM, SBM, etc.)"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    abbreviation = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

class FluidProperty(models.Model):
    """Fluid property model for rheology and other measurements"""
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.unit})"

class FluidSample(models.Model):
    """Fluid sample model for lab data"""
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name='fluid_samples')
    fluid_type = models.ForeignKey(FluidType, on_delete=models.CASCADE)
    sample_name = models.CharField(max_length=100)
    depth = models.DecimalField(max_digits=8, decimal_places=2)
    temperature = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.sample_name} - {self.fluid_type}"

class FluidMeasurement(models.Model):
    """Individual fluid measurement (rheology, density, etc.)"""
    fluid_sample = models.ForeignKey(FluidSample, on_delete=models.CASCADE, related_name='measurements')
    property = models.ForeignKey(FluidProperty, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=4)
    temperature = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    measured_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.fluid_sample.sample_name} - {self.property.name}: {self.value} {self.property.unit}"
