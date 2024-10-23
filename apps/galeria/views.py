import boto3
import os
from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages
from django.db.models import Q
from datetime import datetime



def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})



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

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)

        print("Form data:", request.POST)
        print("File data:", request.FILES)

        if form.is_valid():
            fotografia = form.save(commit=False)  # Salva o formulário mas não grava no banco ainda
            fotografia.usuario = request.user  # Associar o usuário
            
            # Extraindo a imagem do formulário
            imagem = request.FILES['foto']
            # Define o caminho de upload para o S3
            caminho_upload = f'fotos/{fotografia.data_fotografia.strftime("%Y/%m/%d")}/{imagem.name}'

            # Configuração do cliente S3
            s3 = boto3.client(
                's3',
                aws_access_key_id=os.getenv('AWS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_ACCESS_KEY'),
            )

            try:
                # Faz o upload da imagem
                s3.upload_fileobj(imagem, os.getenv('AWS_BUCKET_NAME'), caminho_upload)
                print("Imagem enviada com sucesso!")

                # Atribuindo a URL correta à fotografia
                fotografia.foto = f'https://{os.getenv("AWS_BUCKET_NAME")}.s3.us-east-2.amazonaws.com/{caminho_upload}'

                # Salve o objeto
                fotografia.save()

                # Confirme que a foto foi salva
                print("Fotografia salva com URL:", fotografia.foto)

                messages.success(request, 'Fotografia Cadastrada com sucesso!')
                return redirect('index')
            except Exception as e:
                print(f"Erro ao enviar imagem: {e}")
                messages.error(request, 'Erro ao enviar a fotografia. Tente novamente.')

        else:
            print("Form errors:", form.errors)

    else:
        form = FotografiaForms()

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