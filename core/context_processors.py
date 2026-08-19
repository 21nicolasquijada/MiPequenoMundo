from .models import Configuracion


def configuracion_global(request):
    return {'config_sitio': Configuracion.load()}
