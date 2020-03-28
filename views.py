from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import (ListView, DetailView,)
from .forms import PostForm

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from core.models import Cliente


class ClienteDetailView(generic.DetailView):
    model = Cliente

def formulario_buscar(request):
    return render(request, 'formulario_buscar.html')

def buscar(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menos a 20 caracteres.')
        else:
            cliente = Cliente.objects.filter(nombre__icontains=q)
            return render(request, 'resultados.html',{'cliente':cliente, 'query':q})

    return render(request, 'formulario_buscar.html',{'errors':errors})

"""
def client_detail(request):
    cliente = Cliente.objects.get(pk=1)
    return render(request, 'client_detail.html', {'cliente':cliente})

"""

def client_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'client_detail.html', {'cliente': cliente})
