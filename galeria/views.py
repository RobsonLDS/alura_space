from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):

    '''
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtrlrcope.org / NASA / James Webb"},
        2: {"nome": "Galáxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble"},
    }
    return render(request, 'galeria/index.html', {"cards": dados})
    '''

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_bucar = request.GET['buscar']
        if nome_a_bucar:
            fotografias = fotografias.filter(nome__icontains=nome_a_bucar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})