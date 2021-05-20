from django.shortcuts import render

from .models import Receitas 

def index(request):
    receitas = Receitas.objects.all()

    context = {
        'Receitas': 'Site Django de receitas (iniciante)',
        'outro': 'Receitas simples.',
        'receitas': receitas
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')
