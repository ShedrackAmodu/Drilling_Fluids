from django.db import models


class CalculationRun(models.Model):
    tenant = models.ForeignKey('drillflow.apps.tenants.Tenant', on_delete=models.CASCADE)
    well = models.ForeignKey('drillflow.apps.wells.Well', on_delete=models.CASCADE, null=True, blank=True)
    calculation_type = models.CharField(max_length=100)
    input_snapshot = models.JSONField(default=dict)
    output_results = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calc {self.calculation_type} ({self.id})"
