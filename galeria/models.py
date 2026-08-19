from django.db import models


class FotoGaleria(models.Model):
    titulo = models.CharField(max_length=150, blank=True)
    imagen = models.ImageField(upload_to='galeria/')
    descripcion = models.CharField(max_length=250, blank=True)
    orden = models.PositiveIntegerField(default=0, help_text='Las fotos con número menor aparecen primero')
    subida_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foto de galería'
        verbose_name_plural = 'Fotos de galería'
        ordering = ['orden', '-subida_el']

    def __str__(self):
        return self.titulo or f'Foto {self.pk}'
