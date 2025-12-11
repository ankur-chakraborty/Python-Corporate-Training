from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add'),
    path('edit/<int:pk>/', views.edit_task, name='edit'),
    path('complete/<int:pk>/', views.complete_task, name='complete'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
]