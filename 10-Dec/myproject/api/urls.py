from django.urls import path
# from .views import hello
from .views import employees

# urlpatterns = [
#     path('hello/', hello)
# ]


urlpatterns = [
    path('employees/', employees)
]