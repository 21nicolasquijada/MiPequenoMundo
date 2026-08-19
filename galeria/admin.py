from django.contrib import admin
from django.utils.html import format_html
from .models import FotoGaleria


@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ['miniatura', 'titulo', 'orden', 'subida_el']
    list_editable = ['orden']
    ordering = ['orden', '-subida_el']

    def miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;" />', obj.imagen.url)
        return '—'
    miniatura.short_description = 'Vista previa'
