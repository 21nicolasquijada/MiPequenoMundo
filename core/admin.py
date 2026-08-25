from django.contrib import admin
from django.utils.html import format_html
from .models import Configuracion, Documento, PaginaInicio, PaginaSobreNosotros, Reglamento


class SingletonAdmin(admin.ModelAdmin):
    """Evita crear más de un registro y salta directo a la edición."""

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = self.model.load()
        from django.shortcuts import redirect
        return redirect('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), obj.pk)


@admin.register(Configuracion)
class ConfiguracionAdmin(SingletonAdmin):
    pass


@admin.register(PaginaInicio)
class PaginaInicioAdmin(SingletonAdmin):
    pass


@admin.register(Reglamento)
class ReglamentoAdmin(SingletonAdmin):
    readonly_fields = ['actualizado']


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descarga', 'orden', 'subido_el']
    list_editable = ['orden']
    ordering = ['orden', '-subido_el']

    def descarga(self, obj):
        if obj.archivo:
            return format_html('<a href="{}" target="_blank" rel="noopener">Ver PDF</a>', obj.archivo.url)
        return '—'
    descarga.short_description = 'Archivo'


@admin.register(PaginaSobreNosotros)
class PaginaSobreNosotrosAdmin(SingletonAdmin):
    fieldsets = (
        (None, {'fields': ('imagen_hero',)}),
        ('Bienvenida', {'fields': ('bienvenida',)}),
        ('Misión y visión', {'fields': ('mision', 'vision')}),
        ('Sellos educativos', {'fields': ('sellos_educativos',)}),
        ('Valores y competencias', {'fields': ('valores_intro', 'lista_valores')}),
    )
