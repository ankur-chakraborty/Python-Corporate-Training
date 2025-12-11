from django.urls import path
from .views import employees_api, employee_api

urlpatterns = [
    path('api/employees/', employees_api),
    path('api/employees/<int:id>/', employee_api),
]