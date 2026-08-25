import io

from django.core.files.base import ContentFile
from django.db import models
from PIL import Image, ImageOps

MAX_IMAGE_WIDTH = 1920
JPEG_QUALITY = 82


def optimize_image_field(field_file):
    """Redimensiona (ancho máx. MAX_IMAGE_WIDTH) y recomprime, en el mismo storage, una
    imagen que ya fue guardada en un ImageField. Pensado para dejar las imágenes subidas
    desde /admin listas para producción sin depender de que el usuario las optimice antes."""
    if not field_file:
        return

    field_file.open('rb')
    try:
        image = Image.open(field_file)
        image = ImageOps.exif_transpose(image)
        image.load()
    finally:
        field_file.close()

    fmt = (image.format or 'JPEG').upper()
    if fmt == 'JPG':
        fmt = 'JPEG'

    if image.width > MAX_IMAGE_WIDTH:
        ratio = MAX_IMAGE_WIDTH / float(image.width)
        image = image.resize((MAX_IMAGE_WIDTH, round(image.height * ratio)), Image.LANCZOS)

    buffer = io.BytesIO()
    if fmt == 'JPEG':
        if image.mode in ('RGBA', 'P', 'LA'):
            image = image.convert('RGB')
        image.save(buffer, format='JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)
    elif fmt == 'PNG':
        image.save(buffer, format='PNG', optimize=True)
    elif fmt == 'WEBP':
        image.save(buffer, format='WEBP', quality=JPEG_QUALITY, method=6)
    else:
        image.save(buffer, format=fmt)

    name = field_file.name
    storage = field_file.storage
    if storage.exists(name):
        storage.delete(name)
    storage.save(name, ContentFile(buffer.getvalue()))


class OptimizedImagesModel(models.Model):
    """Modelo base: al guardar, optimiza cada ImageField que acaba de subirse (recién
    asignado y aún no confirmado en el storage), sin volver a comprimir imágenes ya
    guardadas en llamadas a save() posteriores."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        pending = [
            field.name for field in self._meta.get_fields()
            if isinstance(field, models.ImageField)
            and getattr(self, field.name)
            and not getattr(self, field.name)._committed
        ]
        super().save(*args, **kwargs)
        for field_name in pending:
            optimize_image_field(getattr(self, field_name))
