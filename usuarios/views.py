from django.shortcuts import render
from usuarios.forms import Loginforms, Cadastroforms

def login(request):
    form = Loginforms
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = Cadastroforms
    return render(request, 'usuarios/cadastro.html', {'form': form})
