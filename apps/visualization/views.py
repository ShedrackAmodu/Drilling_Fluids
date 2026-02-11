from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Dashboard, ChartWidget
from .services import VisualizationService

def dashboard_view(request, dashboard_id):
    dashboard = get_object_or_404(Dashboard, id=dashboard_id)
    widgets = dashboard.widgets.all()
    return render(request, 'visualization/dashboard.html', {'dashboard': dashboard, 'widgets': widgets})

def widget_data(request, widget_id):
    widget = get_object_or_404(ChartWidget, id=widget_id)
    payload = VisualizationService.render_chart(widget)
    return JsonResponse(payload)
