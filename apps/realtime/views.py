from django.http import JsonResponse
from .models import TimeSeries

def series_latest(request, series_id):
    ts = TimeSeries.objects.get(id=series_id)
    points = ts.points.order_by('-timestamp')[:100]
    data = [{'timestamp': p.timestamp.isoformat(), 'value': p.value} for p in points]
    return JsonResponse({'series': ts.name, 'data': data})
