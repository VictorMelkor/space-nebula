from django.shortcuts import render, get_object_or_404, redirect

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Fotografia

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.filter(publicada=True).order_by("data_fotografia")

    nome_a_buscar = request.GET.get('buscar', '')
    if nome_a_buscar:
        # Filtrando por nome, legenda, descrição e categoria
        fotografias = fotografias.filter(
            Q(nome__icontains=nome_a_buscar) | 
            Q(legenda__icontains=nome_a_buscar) | 
            Q(descricao__icontains=nome_a_buscar) | 
            Q(categoria__icontains=nome_a_buscar)  # Agora inclui a categoria
        )
        
        if not fotografias.exists():
            messages.info(request, 'Nenhuma fotografia encontrada com esse termo.')

    return render(request, "galeria/index.html", {"cards": fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia Cadastrada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')


    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem deleta com sucesso!')

    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    
    return render(request, 'galeria/index.html', {'cards':fotografias})