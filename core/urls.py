from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('documentos/', views.documentos, name='documentos'),
]
