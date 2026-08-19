from django.contrib import admin
from .models import Configuracion, PaginaInicio, Reglamento


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
