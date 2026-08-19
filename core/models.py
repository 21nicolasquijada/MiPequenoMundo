from django.core.exceptions import ValidationError
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class SingletonModel(models.Model):
    """Base para modelos de los que solo debe existir un registro (pk=1)."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    def clean(self):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError('Ya existe un registro de este tipo. Debes editar el existente.')

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Configuracion(SingletonModel):
    nombre_jardin = models.CharField(max_length=150, default='Jardín Infantil Mi Pequeño Mundo')
    lema = models.CharField(max_length=200, blank=True, help_text='Ej: Convivir en armonía, aprender con alegría')
    direccion = models.CharField(max_length=250, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    whatsapp_url = models.URLField(blank=True)
    logo = models.ImageField(upload_to='sitio/', blank=True, null=True)

    class Meta:
        verbose_name = 'Configuración del sitio'
        verbose_name_plural = 'Configuración del sitio'

    def __str__(self):
        return self.nombre_jardin


class PaginaInicio(SingletonModel):
    titulo_hero = models.CharField(max_length=200, default='Bienvenidos a Mi Pequeño Mundo')
    subtitulo_hero = models.CharField(max_length=250, blank=True)
    imagen_hero = models.ImageField(upload_to='inicio/', blank=True, null=True)
    texto_bienvenida = RichTextUploadingField(blank=True)

    class Meta:
        verbose_name = 'Página de inicio'
        verbose_name_plural = 'Página de inicio'

    def __str__(self):
        return 'Contenido de la página de inicio'


class Reglamento(SingletonModel):
    contenido = RichTextUploadingField(blank=True)
    archivo_pdf = models.FileField(upload_to='reglamento/', blank=True, null=True,
                                    help_text='Opcional: versión descargable en PDF')
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reglamento interno'
        verbose_name_plural = 'Reglamento interno'

    def __str__(self):
        return 'Reglamento interno'
