
from django.urls import path
from .views import vehicle_api

urlpatterns = [
    path('vehicles/', vehicle_api),
]
