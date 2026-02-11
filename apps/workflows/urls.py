from django.urls import path
from . import views

urlpatterns = [
    path('', views.workflow_list, name='workflow_list'),
    path('<int:workflow_id>/', views.workflow_detail, name='workflow_detail'),
]
