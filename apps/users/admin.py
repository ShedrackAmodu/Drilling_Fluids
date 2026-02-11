from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, TenantUser

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom admin interface for User model"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

# Register TenantUser for admin management
@admin.register(TenantUser)
class TenantUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'tenant', 'role', 'is_active', 'invited_at', 'joined_at')
    list_filter = ('role', 'is_active', 'tenant')
    search_fields = ('user__email', 'tenant__name')
    ordering = ('-invited_at',)
