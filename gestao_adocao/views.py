from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Adotante
from .forms import AdotanteForm 

# Listar Adoções
def listar_adocoes(request):
    adotantes = Adotante.objects.all()
    return render(request, 'listar_adocoes.html', {'adotantes': adotantes})

# Criar Adoção
def criar_adocao(request):
    if request.method == 'POST':
        form = AdotanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_adocoes')  # Redireciona para a lista após salvar
    else:
        form = AdotanteForm()
    return render(request, 'formulario_adocao.html', {'form': form})

# Edição da adoção
def editar_adocao(request, id):
    adotante = get_object_or_404(Adotante, id=id)
    if request.method == 'POST':
        form = AdotanteForm(request.POST, instance=adotante)
        if form.is_valid():
            form.save()
            return redirect('listar_adocoes')  # Redireciona para a lista após salvar
    else:
        form = AdotanteForm(instance=adotante)
    return render(request, 'editar_adocao.html', {'form': form, 'adotante': adotante})

# Remoção da Adoção
def remover_adocao(request, id):
    adotante = get_object_or_404(Adotante, id=id)
    if request.method == 'POST':
        adotante.delete()
        return redirect('listar_adocoes')  # Redireciona para a lista após remover
    return render(request, 'remover_adocao.html', {'adotante': adotante})


def adote_view(request):
    adotantes = Adotante.objects.all()  # Buscando todos os adotantes
    return render(request, 'gestao_adocao/adote.html', {'adotantes': adotantes})


