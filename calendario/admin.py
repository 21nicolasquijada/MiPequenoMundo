from django.contrib import admin
from core.admin import SingletonAdmin
from .models import EventoCalendario, PaginaCalendario


@admin.register(PaginaCalendario)
class PaginaCalendarioAdmin(SingletonAdmin):
    pass


@admin.register(EventoCalendario)
class EventoCalendarioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_inicio', 'fecha_fin', 'publicado']
    list_editable = ['publicado']
    list_filter = ['publicado']
    date_hierarchy = 'fecha_inicio'
    ordering = ['fecha_inicio']
    fields = ['titulo', 'fecha_inicio', 'fecha_fin', 'hora_inicio', 'hora_fin', 'descripcion', 'imagen', 'publicado']
