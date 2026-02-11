from django.db import models
from apps.users.models import User
from apps.wells.models import Well
from apps.fluids.models import FluidSample
from .services import CalculationService
from .validators import validate_calculation_input
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

class Calculation(models.Model):
    """Calculation model for storing calculation results"""
    CALCULATION_TYPES = [
        ('rheology', 'Rheology Analysis'),
        ('hydraulics', 'Hydraulics'),
        ('ecd', 'Equivalent Circulating Density'),
        ('surge_swab', 'Surge & Swab'),
        ('custom', 'Custom Calculation'),
    ]
    
    name = models.CharField(max_length=100)
    calculation_type = models.CharField(max_length=20, choices=CALCULATION_TYPES)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name='calculations')
    fluid_sample = models.ForeignKey(FluidSample, on_delete=models.CASCADE, null=True, blank=True)
    parameters = models.JSONField(help_text="Calculation parameters as JSON")
    results = models.JSONField(help_text="Calculation results as JSON")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.calculation_type}"

def validate_and_run_rheology(data):
    validate_calculation_input(data)
    pv = CalculationService.calculate_pv(data['θ600'], data['θ300'])
    yp = CalculationService.calculate_yp(data['θ300'], pv)
    av = CalculationService.calculate_av(data['θ600'])
    return {'PV': pv, 'YP': yp, 'AV': av}

class Workflow(models.Model):
    """Workflow model for no-code workflow builder"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    steps = models.JSONField(help_text="Workflow steps as JSON")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class CalculationUnit(models.Model):
    """Model to store unit info for calculation outputs"""
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
