from django.core.exceptions import ValidationError
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from core.models import SingletonModel


class PaginaCalendario(SingletonModel):
    imagen_hero = models.ImageField(upload_to='calendario/', blank=True, null=True)

    class Meta:
        verbose_name = 'Portada de calendario'
        verbose_name_plural = 'Portada de calendario'

    def __str__(self):
        return 'Portada de la página de calendario'


class EventoCalendario(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(
        blank=True, null=True,
        help_text='Déjalo vacío si es un evento de un solo día. Complétalo si abarca '
                   'varios días (por ejemplo, una semana completa).',
    )
    descripcion = RichTextUploadingField(blank=True)
    imagen = models.ImageField(upload_to='calendario/', blank=True, null=True)
    publicado = models.BooleanField(default=True, help_text='Desmarca para ocultarlo del sitio sin borrarlo')

    class Meta:
        verbose_name = 'Evento del calendario'
        verbose_name_plural = 'Eventos del calendario'
        ordering = ['fecha_inicio']

    def clean(self):
        if self.fecha_fin and self.fecha_inicio and self.fecha_fin < self.fecha_inicio:
            raise ValidationError({'fecha_fin': 'No puede ser anterior a la fecha de inicio.'})

    def __str__(self):
        return f'{self.titulo} ({self.fecha_inicio:%d-%m-%Y})'
