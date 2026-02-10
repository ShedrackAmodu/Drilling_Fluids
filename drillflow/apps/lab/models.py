from django.db import models


class RheologyTest(models.Model):
    fluid_system = models.ForeignKey('drillflow.apps.fluids.FluidSystem', on_delete=models.CASCADE)
    rpm_600 = models.FloatField(null=True, blank=True)
    rpm_300 = models.FloatField(null=True, blank=True)
    rpm_200 = models.FloatField(null=True, blank=True)
    rpm_100 = models.FloatField(null=True, blank=True)
    rpm_6 = models.FloatField(null=True, blank=True)
    rpm_3 = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"RheologyTest {self.id} for Fluid {self.fluid_system_id}"
