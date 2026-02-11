from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drillflow.apps.core'
    verbose_name = 'Core Utilities'
