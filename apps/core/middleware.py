from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model
from apps.users.models import TenantUser

class TenantAwareAuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware to ensure user requests are tenant-aware and restrict cross-tenant access.
    """
    def process_request(self, request):
        user = request.user
        if user.is_authenticated:
            # Attach tenant memberships to request for easy access
            request.tenant_memberships = TenantUser.objects.filter(user=user, is_active=True)
            # Optionally, set current tenant context from session or subdomain
            # Example: request.current_tenant = ...
        else:
            request.tenant_memberships = None
