from django.core.exceptions import PermissionDenied
from apps.users.models import TenantUser

def restrict_cross_tenant_access(user, tenant):
    """
    Utility to restrict access to resources outside user's tenant memberships.
    Raise PermissionDenied if user is not a member of the tenant.
    """
    if not user.is_authenticated:
        raise PermissionDenied("User is not authenticated.")
    if not TenantUser.objects.filter(user=user, tenant=tenant, is_active=True).exists():
        raise PermissionDenied("Access denied: cross-tenant access is not allowed.")
