from django.shortcuts import render
from .models import FotoGaleria, PaginaGaleria


def galeria(request):
    context = {
        'fotos': FotoGaleria.objects.all(),
        'portada': PaginaGaleria.load(),
    }
    return render(request, 'galeria/galeria.html', context)
