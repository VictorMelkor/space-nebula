# example/views.py
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from example.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'imagem.html', {"fotografia": fotografia})