from django.contrib import admin
from .models import Address, Categoria,Producto,Cliente, Encargado, Orden, Factura,Inventario,Articulo, Rol, ArticuloInstance


###########################################

###########################################33#
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    pass
################################################33

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre',
			'apellido',
			'empresa')
	list_filter = ('empresa',)
	search_fields = ('nombre','apellido','empresa')

admin.site.register(Cliente, ClienteAdmin)
#######################################################

#admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Rol)
admin.site.register(Inventario)
admin.site.register(Articulo)
#admin.site.register(Factura)
admin.site.register(Encargado)
admin.site.register(Orden)
#admin.site.register(Cliente)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'detalles', 'precio','cantidad','disponible']
    list_editable = ['precio', 'disponible']
admin.site.register(Categoria)
