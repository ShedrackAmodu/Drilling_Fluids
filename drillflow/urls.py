from django.urls import path, include
from django.http import HttpResponse
from django.contrib import admin


def health(request):
    return HttpResponse('OK')


urlpatterns = [
    path('health/', health),
    path('admin/', admin.site.urls),
]
