from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
