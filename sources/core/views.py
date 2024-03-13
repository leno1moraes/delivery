from django.shortcuts import render

from .models import Unidade, Produto

def index(request):
    produtos = Produto.objects.all();

    context = {
        'empresa' : 'Delivery rápido',
        'recado' : 'Veja a lista de hoje',
        'produtos' : produtos
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')