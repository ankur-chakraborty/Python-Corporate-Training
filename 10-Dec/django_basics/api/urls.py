from django.urls import path
from .views import hello, welcome, status
urlpatterns = [
    path('hello/', hello),
    path(' welcome/', welcome),
    path(' status/', status)

]