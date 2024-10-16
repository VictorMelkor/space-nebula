# example/urls.py
from django.urls import path

from fotografias.views import index, imagem, buscar


urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar')
]