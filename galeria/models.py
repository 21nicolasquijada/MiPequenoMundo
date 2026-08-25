import re

from django.core.exceptions import ValidationError
from django.db import models
from core.models import SingletonModel
from core.utils import OptimizedImagesModel

YOUTUBE_ID_RE = re.compile(r'(?:youtube\.com/(?:watch\?v=|embed/|shorts/)|youtu\.be/)([\w-]{11})')


class PaginaGaleria(OptimizedImagesModel, SingletonModel):
    imagen_hero = models.ImageField(upload_to='galeria/', blank=True, null=True)

    class Meta:
        verbose_name = 'Portada de galería'
        verbose_name_plural = 'Portada de galería'

    def __str__(self):
        return 'Portada de la página de galería'


class FotoGaleria(OptimizedImagesModel):
    titulo = models.CharField(max_length=150, blank=True)
    imagen = models.ImageField(
        upload_to='galeria/', blank=True, null=True,
        help_text='Para un video de YouTube puedes dejarla vacía: se usará la miniatura del video.',
    )
    video_url = models.URLField(
        'Enlace de YouTube', blank=True,
        help_text='Si se completa, la tarjeta enlaza directo a este video de YouTube en vez de abrir la foto en grande.',
    )
    descripcion = models.CharField(max_length=250, blank=True)
    orden = models.PositiveIntegerField(default=0, help_text='Las fotos con número menor aparecen primero')
    subida_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foto de galería'
        verbose_name_plural = 'Fotos de galería'
        ordering = ['orden', '-subida_el']

    def __str__(self):
        return self.titulo or f'Foto {self.pk}'

    def clean(self):
        if not self.imagen and not self.video_url:
            raise ValidationError('Debes subir una imagen o indicar el enlace de un video de YouTube.')

    @property
    def youtube_id(self):
        if not self.video_url:
            return ''
        match = YOUTUBE_ID_RE.search(self.video_url)
        return match.group(1) if match else ''

    @property
    def miniatura_url(self):
        if self.imagen:
            return self.imagen.url
        youtube_id = self.youtube_id
        if youtube_id:
            return f'https://img.youtube.com/vi/{youtube_id}/hqdefault.jpg'
        return ''
