from django.shortcuts import get_object_or_404, render
from .models import Anuncio
from django.http import Http404

def index(request):
    anuncios = Anuncio.objects.order_by('-pub_date')
    context = {'anuncios': anuncios,}
    return render(request, 'anuncios/index.html', context)

def detail(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    return render(request, 'anuncios/detail.html', {'anuncio': anuncio})