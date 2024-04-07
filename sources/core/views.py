from django.shortcuts import render, redirect
from .models import Unidade, Produto
from django.contrib.auth.forms import UserCreationForm

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