from django.urls import path
from . import views

urlpatterns = [
    path('dashboards/<int:dashboard_id>/', views.dashboard_view, name='dashboard_view'),
    path('widgets/<int:widget_id>/data/', views.widget_data, name='widget_data'),
]
