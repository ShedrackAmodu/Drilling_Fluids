from django.db import models


class Rig(models.Model):
    tenant = models.ForeignKey('drillflow.apps.tenants.Tenant', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Well(models.Model):
    tenant = models.ForeignKey('drillflow.apps.tenants.Tenant', on_delete=models.CASCADE)
    rig = models.ForeignKey(Rig, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    spud_date = models.DateField(null=True, blank=True)
    depth_md = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class WellSection(models.Model):
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name='sections')
    section_name = models.CharField(max_length=200)
    hole_size = models.FloatField(null=True, blank=True)
    casing_size = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.well.name} - {self.section_name}"
