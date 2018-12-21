from django.contrib import admin
from .models import Categoria,Producto,Pedido,Cliente,Renta


#admin.site.register(Cliente)
#admin.site.register(Pedido)
#admin.site.register(Producto)
#admin.site.register(Renta)


class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre',
			'apellido',
			'celular',
			'empresa')
	list_filter = ('empresa',)

admin.site.register(Cliente, ClienteAdmin)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('producto',
			'detalles',
			'precio',
			'cantidad',
			'display_Categoria')

	list_filter = ('categoria',)

	fields = [('producto','detalles'),
		('precio','cantidad','categoria')]


class RentaInLine(admin.TabularInline):
	model = Renta

@admin.register(Renta)
class RentaAdmin(admin.ModelAdmin):
	
	list_display = ('producto','cantidad')



@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display  = ('cliente',
			'estado_de_renta',
			'date_deliver',
			'date_receive')
	
	list_filter = ('estado_de_renta',
			'tipo_de_entrega',
			'pago_pendiente',
			'estado_de_pago')
"""
	fieldsets = (
		(None, {
			'fields':['id','cliente',
				'renta']
			}),
		('Control de fechas',{
			'fields':[('date_deliver',
				'date_receive',
				'date_return')]
			}),
		('Estados del pedido',{
			'fields':[('estado_de_renta',
				'estado_de_pago',
				'tipo_de_entrega')]
			}),
		('Pendientes',{
			'fields':[('pago_pendiente',
				'deposito')]
			}),
		('Datos Adicionales',{
			'fields':('direccion',
				'observacion')
			}),
		)
"""
admin.site.register(Categoria)

