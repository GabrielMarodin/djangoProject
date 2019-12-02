from django.shortcuts import get_object_or_404, render
from .models import Anuncio
from .forms import AnuncioForm
from django.http import Http404, HttpResponseRedirect
from user.models import User

def index(request):
    anuncios = Anuncio.objects.order_by('-data_cadastro')
    context = {'anuncios': anuncios,}
    return render(request, 'anuncios/anuncios.html', context)

def detail(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, pk=anuncio_id)
    return render(request, 'anuncios/detail.html', {'anuncio': anuncio})

def create(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnuncioForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            new_anuncio = form.save(commit=False)
            new_anuncio.user = user
            new_anuncio.save()
            form.save_m2m()
            return HttpResponseRedirect('/anuncios/')

    else:
        form = AnuncioForm()

    return render(request, 'anuncios/create.html', {'form': form})
