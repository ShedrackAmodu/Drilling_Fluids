from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.core.models import Tenant
from .models import TenantUser

@login_required
def admin_tenant_management(request):
    """
    Admin UI for managing tenants and users (placeholder view).
    """
    # Only allow users with admin role in any tenant
    admin_memberships = TenantUser.objects.filter(user=request.user, role='admin', is_active=True)
    if not admin_memberships.exists():
        return redirect('no_permission')
    tenants = Tenant.objects.all()
    return render(request, 'admin/tenant_management.html', {'tenants': tenants, 'admin_memberships': admin_memberships})

def invite_user_to_tenant(email, tenant, role='client'):
    """
    Send an invitation to a user to join a tenant. Creates a TenantUser entry with is_active=False.
    """
    User = get_user_model()
    user, created = User.objects.get_or_create(email=email, defaults={'username': email.split('@')[0]})
    tenant_user, created = TenantUser.objects.get_or_create(user=user, tenant=tenant, defaults={'role': role, 'is_active': False})
    # Generate invitation token (for real use, store and validate this securely)
    token = get_random_string(32)
    invite_url = settings.SITE_URL + reverse('accept_invite', args=[token])
    send_mail(
        subject='You are invited to DrillFlow',
        message=f'You have been invited to join {tenant.name} as {role}. Accept: {invite_url}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
    return tenant_user, token
