from django.shortcuts import render

from anuncios.models import Anuncio 
from anuncios.choices import estado_choices, quarto_choices, preco_choices

def index(request):
    anuncios = Anuncio.objects.order_by('-data_cadastro').filter(publicado=True)[:3]
    
    context = {
        'anuncios': anuncios,
        'estado_choices': estado_choices,
        'quarto_choices': quarto_choices,
        'preco_choices': preco_choices
    }
    return render(request, 'paginas/index.html', context)

def about(request):
    pass