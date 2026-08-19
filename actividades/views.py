from django.shortcuts import render
from .models import PaginaActividades, SemanaActividades


def actividades(request):
    context = {
        'semanas': SemanaActividades.objects.filter(publicada=True),
        'portada': PaginaActividades.load(),
    }
    return render(request, 'actividades/actividades.html', context)
