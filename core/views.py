from django.shortcuts import render
from actividades.models import SemanaActividades
from galeria.models import FotoGaleria
from .models import PaginaInicio, Reglamento


def inicio(request):
    ultima_semana = SemanaActividades.objects.filter(publicada=True).first()
    context = {
        'inicio': PaginaInicio.load(),
        'ultima_semana': ultima_semana,
        'dias_recientes': ultima_semana.dias[:3] if ultima_semana else [],
        'fotos_destacadas': FotoGaleria.objects.all()[:6],
    }
    return render(request, 'core/inicio.html', context)


def reglamento(request):
    context = {'reglamento': Reglamento.load()}
    return render(request, 'core/reglamento.html', context)
