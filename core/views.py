from django.shortcuts import render, redirect
from .models import Pessoa
from.forms import PessoaForm


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def nova_pesssoa(request):
    form = PessoaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, 'pessoas-form.html', {'form': form})

def update_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)  # instacia e para o form ja começar preenchido

    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')

    return render(request, 'pessoas-form.html', {'form': form, 'pessoa': pessoa})

