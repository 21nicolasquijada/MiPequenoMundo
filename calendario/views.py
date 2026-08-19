from datetime import date
from itertools import groupby

from django.shortcuts import render
from .models import EventoCalendario


def calendario(request):
    eventos = EventoCalendario.objects.filter(publicado=True)
    meses = [
        {'fecha_referencia': date(year, month, 1), 'eventos': list(grupo)}
        for (year, month), grupo in groupby(eventos, key=lambda e: (e.fecha_inicio.year, e.fecha_inicio.month))
    ]
    return render(request, 'calendario/calendario.html', {'meses': meses})
