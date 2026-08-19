from django.contrib import admin
from .models import SemanaActividades


@admin.register(SemanaActividades)
class SemanaActividadesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'fecha_inicio', 'publicada']
    list_editable = ['publicada']
    ordering = ['-fecha_inicio']
    fieldsets = (
        (None, {'fields': ('fecha_inicio', 'publicada')}),
        ('Lunes', {'fields': ('lunes_descripcion', 'lunes_imagen')}),
        ('Martes', {'fields': ('martes_descripcion', 'martes_imagen')}),
        ('Miércoles', {'fields': ('miercoles_descripcion', 'miercoles_imagen')}),
        ('Jueves', {'fields': ('jueves_descripcion', 'jueves_imagen')}),
        ('Viernes', {'fields': ('viernes_descripcion', 'viernes_imagen')}),
    )
