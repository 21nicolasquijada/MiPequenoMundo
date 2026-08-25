from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import OptimizedImagesModel


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


class Configuracion(OptimizedImagesModel, SingletonModel):
    nombre_jardin = models.CharField(max_length=150, default='Jardín Infantil Mi Pequeño Mundo')
    lema = models.CharField(max_length=200, blank=True, help_text='Ej: Convivir en armonía, aprender con alegría')
    direccion = models.CharField(max_length=250, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    whatsapp_url = models.URLField(blank=True)
    blog_url = models.URLField(
        'Enlace del blog', blank=True, default='https://mipequenomundo2011.blogspot.com/',
        help_text='Se muestra como sección y enlace en el sitio. Déjalo vacío para ocultarlo.',
    )
    logo = models.ImageField(upload_to='sitio/', blank=True, null=True)

    class Meta:
        verbose_name = 'Configuración del sitio'
        verbose_name_plural = 'Configuración del sitio'

    def __str__(self):
        return self.nombre_jardin


class PaginaInicio(OptimizedImagesModel, SingletonModel):
    titulo_hero = models.CharField(max_length=200, default='Bienvenidos a Mi Pequeño Mundo')
    subtitulo_hero = models.CharField(max_length=250, blank=True)
    imagen_hero = models.ImageField(upload_to='inicio/', blank=True, null=True)
    texto_bienvenida = RichTextUploadingField(blank=True)

    class Meta:
        verbose_name = 'Página de inicio'
        verbose_name_plural = 'Página de inicio'

    def __str__(self):
        return 'Contenido de la página de inicio'


DEFAULT_BIENVENIDA = (
    '<p>Reciban un afectuoso saludo de bienvenida. Agradecemos la confianza que han depositado '
    'en nuestro jardín: tengan la seguridad de que en <strong>Mi Pequeño Mundo</strong> sus hijos '
    'e hijas encontrarán un espacio seguro para crecer en armonía y aprender con alegría, con '
    'nuestro amor y dedicación.</p>'
    '<p>Para muchas familias es un lugar nuevo. De a poco, día a día, los niños y niñas irán '
    'adquiriendo confianza y seguridad, descubriendo un mundo especial de risas, compañeritos, '
    'juegos, cantos y colores — también algunos desencuentros que sabremos acompañar como '
    'mediadores, para compartir en sana convivencia.</p>'
    '<p>Los invitamos a mantener una comunicación constante, basada en el respeto y la '
    'comprensión mutuos, y a vivir día a día el clima familiar y cercano que esperamos para '
    'nuestra comunidad escolar. Ya son parte de la gran familia Mi Pequeño Mundo.</p>'
)

DEFAULT_MISION = (
    '<p>Ser un jardín infantil que se compromete con la educación integral y de calidad de sus '
    'niños y niñas, poniendo énfasis en el desarrollo de las diversas áreas de la educación '
    'parvularia, con un enfoque de altas expectativas, en un ambiente de sana convivencia, '
    'ecológico e inclusivo, donde se respeta la diversidad, de modo que sepan adaptarse con '
    'armonía a los cambios de su entorno, proyectándose a una vida futura a través de '
    'experiencias significativas en los procesos educativos.</p>'
)

DEFAULT_VISION = (
    '<p>En nuestro jardín infantil pretendemos que los alumnos y alumnas, al finalizar su '
    'proceso educativo, alcancen los objetivos de aprendizaje que les permitan insertarse '
    'exitosamente en el ámbito escolar, convirtiéndose en ciudadanos insertos y participativos, '
    'con valores permanentes de respeto a sí mismos, su entorno social y el medio ambiente.</p>'
)

DEFAULT_SELLOS_EDUCATIVOS = (
    '<h3>Aprender a vivir en armonía</h3>'
    '<p>Lograr un equilibrio en los pensamientos, acciones y sentimientos de los niños y niñas, '
    'para que disfruten cada momento del proceso de enseñanza-aprendizaje, desarrollando '
    'habilidades blandas que faciliten su interacción con el entorno y generando en toda la '
    'comunidad escolar un clima de sana convivencia, respetuosa, asertiva y afectuosa.</p>'
    '<h3>Educar para la vida, formando agentes de cambio</h3>'
    '<p>Educar en los niños y niñas las habilidades para adaptarse con flexibilidad a los '
    'cambios permanentes de su entorno, de manera que apliquen sus experiencias y aprendizajes '
    'para lograr una inserción escolar y social exitosa.</p>'
    '<h3>Experiencias significativas</h3>'
    '<p>Entregar a cada niño y niña vivencias y experiencias pedagógicas de conocimientos y '
    'habilidades con un sentido real para el desarrollo de su vida integral, siempre en la '
    'búsqueda de una educación inclusiva, integradora y de calidad.</p>'
)

DEFAULT_VALORES_INTRO = (
    '<p>El sustento de nuestros valores institucionales son los valores humanistas, basados en '
    'el respeto del ser humano y de este con su entorno social: un ser libre, capaz de reconocer '
    'sus fortalezas y debilidades y de ver lo mismo en quienes lo rodean. Estos valores guían a '
    'toda nuestra comunidad escolar.</p>'
)

DEFAULT_LISTA_VALORES = (
    'Dignidad, Autonomía, Diversidad, Responsabilidad, Templanza, Creatividad, Libertad, '
    'Respeto, Empatía, Alegría, Verdad, Honestidad, Bondad, Gratitud, Justicia, Cooperación, '
    'Solidaridad'
)


class PaginaSobreNosotros(OptimizedImagesModel, SingletonModel):
    imagen_hero = models.ImageField(upload_to='sobre-nosotros/', blank=True, null=True)
    bienvenida = RichTextUploadingField('Mensaje de bienvenida', blank=True, default=DEFAULT_BIENVENIDA)
    mision = RichTextUploadingField('Misión', blank=True, default=DEFAULT_MISION)
    vision = RichTextUploadingField('Visión', blank=True, default=DEFAULT_VISION)
    sellos_educativos = RichTextUploadingField('Sellos educativos', blank=True, default=DEFAULT_SELLOS_EDUCATIVOS)
    valores_intro = RichTextUploadingField('Introducción a valores y competencias', blank=True,
                                            default=DEFAULT_VALORES_INTRO)
    lista_valores = models.TextField(
        'Valores institucionales', blank=True, default=DEFAULT_LISTA_VALORES,
        help_text='Lista de valores separados por coma. Se muestran como etiquetas en la página.',
    )

    class Meta:
        verbose_name = 'Página Sobre Nosotros'
        verbose_name_plural = 'Página Sobre Nosotros'

    def __str__(self):
        return 'Contenido de la página Sobre Nosotros'

    @property
    def valores(self):
        return [valor.strip() for valor in self.lista_valores.split(',') if valor.strip()]


class Reglamento(OptimizedImagesModel, SingletonModel):
    imagen_hero = models.ImageField(upload_to='reglamento/', blank=True, null=True)
    contenido = RichTextUploadingField(
        'Texto introductorio', blank=True,
        help_text='Texto opcional que se muestra sobre la lista de documentos.',
    )
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Página de Documentos'
        verbose_name_plural = 'Página de Documentos'

    def __str__(self):
        return 'Página de Documentos'


class Documento(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250, blank=True)
    archivo = models.FileField(
        upload_to='documentos/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text='Solo se permiten archivos PDF.',
    )
    orden = models.PositiveIntegerField(default=0, help_text='Los documentos con número menor aparecen primero')
    subido_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['orden', '-subido_el']

    def __str__(self):
        return self.titulo
