from django.db import models
from decimal import Decimal
from .compliance import (
    check_api_rp_13b_compliance, lock_parameter, is_parameter_locked,
    set_company_override, get_company_override, set_regional_flag, get_regional_flag,
    set_assumption, get_assumption, add_validation_warning, get_validation_warnings,
    set_compliance_mode, get_compliance_mode, export_standards_summary
)

# Tenant (Company) model for multi-tenant support
class Tenant(models.Model):
	name = models.CharField(max_length=100, unique=True)
	domain = models.CharField(max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

# --- Unit normalization utility ---
UNIT_CONVERSIONS = {
    # Example: 'ft' to 'm'
    ('ft', 'm'): lambda x: x * Decimal('0.3048'),
    ('m', 'ft'): lambda x: x / Decimal('0.3048'),
    # Add more as needed
}

def normalize_unit(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    key = (from_unit, to_unit)
    if key in UNIT_CONVERSIONS:
        return UNIT_CONVERSIONS[key](Decimal(value))
    raise ValueError(f"No conversion from {from_unit} to {to_unit}")

# --- Domain constraint validation utility ---
def validate_domain_constraints(instance):
    """
    Example: Validate that depth_start < depth_end for WellSection, etc.
    """
    if hasattr(instance, 'depth_start') and hasattr(instance, 'depth_end'):
        if instance.depth_start >= instance.depth_end:
            raise ValueError("depth_start must be less than depth_end")
    # Add more domain-specific checks as needed
