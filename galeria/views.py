from django.shortcuts import render
from .models import FotoGaleria


def galeria(request):
    return render(request, 'galeria/galeria.html', {'fotos': FotoGaleria.objects.all()})
