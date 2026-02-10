from django.contrib import admin
from .models import Rig, Well, WellSection


@admin.register(Rig)
class RigAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')


@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rig', 'spud_date', 'depth_md')
    search_fields = ('name',)


@admin.register(WellSection)
class WellSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'well', 'section_name', 'hole_size', 'casing_size')
