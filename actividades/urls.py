from django.urls import path
from . import views

app_name = 'actividades'

urlpatterns = [
    path('', views.actividades, name='actividades'),
]
