from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from core.models import SingletonModel
from core.utils import OptimizedImagesModel


class PaginaActividades(OptimizedImagesModel, SingletonModel):
    imagen_hero = models.ImageField(upload_to='actividades/', blank=True, null=True)

    class Meta:
        verbose_name = 'Portada de actividades'
        verbose_name_plural = 'Portada de actividades'

    def __str__(self):
        return 'Portada de la página de actividades'


class SemanaActividades(OptimizedImagesModel):
    fecha_inicio = models.DateField(
        unique=True,
        help_text='Selecciona el día lunes de la semana que corresponde.',
    )
    publicada = models.BooleanField(default=True, help_text='Desmarca para ocultarla del sitio sin borrarla')

    descripcion_general = RichTextUploadingField(
        'Descripción general de la semana', blank=True,
        help_text='Resumen o presentación general de las actividades de la semana (opcional).',
    )

    lunes_descripcion = RichTextUploadingField('Lunes', blank=True)
    lunes_imagen = models.ImageField('Imagen del lunes', upload_to='actividades/', blank=True, null=True)

    martes_descripcion = RichTextUploadingField('Martes', blank=True)
    martes_imagen = models.ImageField('Imagen del martes', upload_to='actividades/', blank=True, null=True)

    miercoles_descripcion = RichTextUploadingField('Miércoles', blank=True)
    miercoles_imagen = models.ImageField('Imagen del miércoles', upload_to='actividades/', blank=True, null=True)

    jueves_descripcion = RichTextUploadingField('Jueves', blank=True)
    jueves_imagen = models.ImageField('Imagen del jueves', upload_to='actividades/', blank=True, null=True)

    viernes_descripcion = RichTextUploadingField('Viernes', blank=True)
    viernes_imagen = models.ImageField('Imagen del viernes', upload_to='actividades/', blank=True, null=True)

    class Meta:
        verbose_name = 'Semana de actividades'
        verbose_name_plural = 'Semanas de actividades'
        ordering = ['-fecha_inicio']

    def clean(self):
        if self.fecha_inicio and self.fecha_inicio.weekday() != 0:
            raise ValidationError({'fecha_inicio': 'Debe ser un día lunes.'})

    @property
    def fecha_fin(self):
        return self.fecha_inicio + timedelta(days=4)

    @property
    def dias(self):
        campos = [
            ('Lunes', self.lunes_descripcion, self.lunes_imagen, 0),
            ('Martes', self.martes_descripcion, self.martes_imagen, 1),
            ('Miércoles', self.miercoles_descripcion, self.miercoles_imagen, 2),
            ('Jueves', self.jueves_descripcion, self.jueves_imagen, 3),
            ('Viernes', self.viernes_descripcion, self.viernes_imagen, 4),
        ]
        return [
            {
                'nombre': nombre, 'descripcion': descripcion, 'imagen': imagen,
                'fecha': self.fecha_inicio + timedelta(days=offset),
            }
            for nombre, descripcion, imagen, offset in campos if descripcion
        ]

    def __str__(self):
        return f'Semana del {self.fecha_inicio:%d-%m-%Y}'
