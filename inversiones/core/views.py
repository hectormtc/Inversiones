from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import (ListView, DetailView,)
from .forms import PostForm

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from core.models import Cliente, Producto, Categoria, Factura, Orden, Articulo

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


class ClienteDetailView(generic.DetailView):
    model = Cliente

def formulario_buscar(request):
    return render(request, 'account/formulario_buscar.html')

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
            return render(request, 'account/resultados.html',{'cliente':cliente, 'query':q})

    return render(request, 'account/formulario_buscar.html',{'errors':errors})

"""
def client_detail(request):
    cliente = Cliente.objects.get(pk=1)
    return render(request, 'client_detail.html', {'cliente':cliente})

"""

def client_list(request):
    cliente = Cliente.objects.all()
    return render(request,'account/client_list.html', {'cliente':cliente})

def client_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'account/client_detail.html', {'cliente': cliente})


def producto_lista(request, category_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.all() #filter(disponible=True)
    if category_slug:
        categoria = get_object_or_404(Categoria, slug=categoria)
        productos = Producto.filter(categoria=categoria)
    return render(request,
                  'producto/lista.html',
                  {'categoria':categoria,
                  'categorias':categorias,
                  'productos':productos})

def producto_detalle(request, id, slug):
    producto = get_object_or_404(Producto,
                                 id=id,
                                 slug=slug,
                                 disponible=True)
    return render(request,
                  'producto/detalle.html',
                  {'producto':producto})


def factura_lista(request):
    factura = Factura.objects.all()
    return render(request, 'orden/factura_lista.html',
                            {'factura':factura})

def factura_detail(request, pk):
    factura = get_object_or_404(Factura.objects.all(), pk=pk)
    return render(request, 'orden/factura_detail.html',
                 {'factura':factura})



def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('A new user has been successfully registered!')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def user_dashboard(request):
    return render(request, 'dashboard.html')
