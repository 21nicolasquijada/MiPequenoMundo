from django.urls import path
from . import views

app_name = 'galeria'

urlpatterns = [
    path('', views.galeria, name='galeria'),
]
