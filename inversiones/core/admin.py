from django.contrib import admin
from .models import Phone, Address, Categoria,Producto,Cliente, Encargado, Orden, Factura,Inventario,Articulo, Rol, FacturaInstance, ArticuloInstance


class ArticuloInLine(admin.TabularInline):
    model = ArticuloInstance
@admin.register(Articulo)

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad')
    inlines = [ArticuloInLine]
###########################################
@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('articulo',)

#############################################
class FacturaInstanceInLine(admin.TabularInline):
    model =  FacturaInstance
###########################################33#
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display  = ('cliente',)
    inlines = [FacturaInstanceInLine]

class FacturaInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'orden',
    'estado_de_pago'
    'estado_de_renta',
    'date_deliver',
    'date_receive')
    list_filter = ('estado_de_renta',
    'tipo_de_entrega',
    'pago_pendiente',
    'estado_de_pago')
    search_fields = ('nombre','apellido','empresa')
################################################33

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre',
			'apellido',
			'empresa')
	list_filter = ('empresa',)
	search_fields = ('nombre','apellido','empresa')

admin.site.register(Cliente, ClienteAdmin)
#######################################################

admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Rol)
admin.site.register(Inventario)
#admin.site.register(Articulo)
#admin.site.register(Factura)
admin.site.register(Encargado)
#admin.site.register(Orden)
#admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Categoria)
