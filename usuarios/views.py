from django.shortcuts import render
from usuarios.forms import Loginforms

def login(request):
    form = Loginforms
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
