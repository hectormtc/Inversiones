from django.conf.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('clientes',
	 views.ListaClientes.as_view(),
         name='ListaClientes'),
]
