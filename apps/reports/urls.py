from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.template_list, name='report_template_list'),
    path('generate/<int:template_id>/', views.generate_report, name='generate_report'),
]
