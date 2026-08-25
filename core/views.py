from django.shortcuts import render
from actividades.models import SemanaActividades
from galeria.models import FotoGaleria
from .models import Documento, PaginaInicio, PaginaSobreNosotros, Reglamento


def inicio(request):
    ultima_semana = SemanaActividades.objects.filter(publicada=True).first()
    context = {
        'inicio': PaginaInicio.load(),
        'ultima_semana': ultima_semana,
        'dias_recientes': ultima_semana.dias[:3] if ultima_semana else [],
        'fotos_destacadas': FotoGaleria.objects.all()[:6],
    }
    return render(request, 'core/inicio.html', context)


def documentos(request):
    context = {
        'reglamento': Reglamento.load(),
        'documentos': Documento.objects.all(),
    }
    return render(request, 'core/documentos.html', context)


def sobre_nosotros(request):
    context = {'sobre_nosotros': PaginaSobreNosotros.load()}
    return render(request, 'core/sobre_nosotros.html', context)
