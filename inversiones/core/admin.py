from django.contrib import admin
from .models import Categoria,Producto,Orden,Pedido,Cliente


admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Pedido)
admin.site.register(Cliente)
