from django.contrib import admin
from django.utils.html import format_html
from core.admin import SingletonAdmin
from .models import FotoGaleria, PaginaGaleria


@admin.register(PaginaGaleria)
class PaginaGaleriaAdmin(SingletonAdmin):
    pass


@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ['miniatura', 'titulo', 'video_url', 'orden', 'subida_el']
    list_editable = ['orden']
    ordering = ['orden', '-subida_el']

    def miniatura(self, obj):
        url = obj.miniatura_url
        if url:
            return format_html('<img src="{}" style="height:50px;border-radius:4px;" />', url)
        return '—'
    miniatura.short_description = 'Vista previa'
