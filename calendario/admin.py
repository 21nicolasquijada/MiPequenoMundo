from django.contrib import admin
from .models import EventoCalendario


@admin.register(EventoCalendario)
class EventoCalendarioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_inicio', 'fecha_fin', 'publicado']
    list_editable = ['publicado']
    list_filter = ['publicado']
    date_hierarchy = 'fecha_inicio'
    ordering = ['fecha_inicio']
    fields = ['titulo', 'fecha_inicio', 'fecha_fin', 'descripcion', 'imagen', 'publicado']
