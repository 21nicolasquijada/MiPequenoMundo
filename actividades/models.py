from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SemanaActividades(models.Model):
    fecha_inicio = models.DateField(
        unique=True,
        help_text='Selecciona el día lunes de la semana que corresponde.',
    )
    publicada = models.BooleanField(default=True, help_text='Desmarca para ocultarla del sitio sin borrarla')

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
            ('Lunes', self.lunes_descripcion, self.lunes_imagen),
            ('Martes', self.martes_descripcion, self.martes_imagen),
            ('Miércoles', self.miercoles_descripcion, self.miercoles_imagen),
            ('Jueves', self.jueves_descripcion, self.jueves_imagen),
            ('Viernes', self.viernes_descripcion, self.viernes_imagen),
        ]
        return [
            {'nombre': nombre, 'descripcion': descripcion, 'imagen': imagen}
            for nombre, descripcion, imagen in campos if descripcion
        ]

    def __str__(self):
        return f'Semana del {self.fecha_inicio:%d-%m-%Y}'
