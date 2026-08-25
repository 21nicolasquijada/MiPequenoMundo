from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve as serve_static

admin.site.site_header = 'Mi Pequeño Mundo - Administración'
admin.site.site_title = 'Mi Pequeño Mundo'
admin.site.index_title = 'Panel de administración'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('galeria/', include('galeria.urls')),
    path('actividades/', include('actividades.urls')),
    path('calendario/', include('calendario.urls')),
    path('', include('core.urls')),
]

# Los archivos estáticos los sirve WhiteNoise (middleware) en cualquier entorno.
# Los archivos de media (PDFs, fotos subidas) los sirve Django directamente, en
# cualquier entorno (a diferencia del helper static(), que se desactiva solo si
# DEBUG=False): el sitio es de bajo tráfico y no justifica un storage externo.
urlpatterns += [
    re_path(
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
        serve_static,
        {'document_root': settings.MEDIA_ROOT},
    ),
]
