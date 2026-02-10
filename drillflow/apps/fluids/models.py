from django.db import models


class FluidSystem(models.Model):
    FLUID_TYPES = [
        ('WBM', 'Water Based Mud'),
        ('OBM', 'Oil Based Mud'),
        ('SBM', 'Synthetic Based Mud'),
    ]
    tenant = models.ForeignKey('drillflow.apps.tenants.Tenant', on_delete=models.CASCADE)
    well = models.ForeignKey('drillflow.apps.wells.Well', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=10, choices=FLUID_TYPES)
    density = models.FloatField(null=True, blank=True)
    oil_water_ratio = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_display()} ({self.id})"
