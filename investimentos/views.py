from django.shortcuts import render, redirect
from .forms import InvestimentoForm
from .models import Investimento
# Create your views here.


def listar_investimentos(request):
    investimentos = Investimento.objects.all() 
    return render(request, 'investimentos/listar_investimentos.html', {'investimentos': investimentos}) 


def cadastrar_investimentos(request):
    if request.method == 'POST':
        form = InvestimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_investimentos')
    else:
        form = InvestimentoForm()
    return render(request, 'investimentos/cadastrar.html', {'form': form})


def listar_investimento_id(request, id):
    investimento = Investimento.objects.get(id=id)
    return render(request, 'investimentos/lista_investimentos.html', {'investimento':investimento})


def editar_investimento(request, id):
    investimento = Investimento.objects.get(id=id)
    form = InvestimentoForm(request.POST or None, instance=investimento)
    if form.is_valid():
        form.save()
        return redirect('listar_investimentos')
    return render(request, 'investimentos/cadastrar.html', {'form': form})


def remover_investimento(request, id):
    investimento = Investimento.objects.get(id=id)
    if request.method == 'POST':
        investimento.delete()
        return redirect('listar_investimentos')
    return render(request, 'investimentos/confirma_exclusao.html', {'investimento': investimento})