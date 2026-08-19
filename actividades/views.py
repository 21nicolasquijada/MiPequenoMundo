from django.shortcuts import render
from .models import SemanaActividades


def actividades(request):
    semanas = SemanaActividades.objects.filter(publicada=True)
    return render(request, 'actividades/actividades.html', {'semanas': semanas})
