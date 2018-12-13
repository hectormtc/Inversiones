from django.db import models
from datetime import date
from django.urls import reverse
import uuid

class Categoria(models.Model):
	categoria = models.CharField(max_length=50, help_text="Tipo de categoria")

	def __str__(self):
            return self.categoria


class Producto(models.Model):
	producto  = models.CharField(max_length=200, help_text="Nombre del producto")
	detalles  = models.TextField(help_text="Detalles sobre el producto",blank=True)
	precio    = models.PositiveIntegerField()
	cantidad  = models.PositiveIntegerField()
	categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return '{0} {1}'.format(self.producto, self.detalles)

class Renta(models.Model):
	producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
	cantidad = models.PositiveIntegerField()

	def getSubtotal(self):
		return self.cantidad * self.producto.precio


	def __str__(self):
		return 'Producto: {0}, Cantidad: {1}, Subtotal: {2}'.format(
													self.producto,
													self.cantidad,
													self.getSubtotal())

class Cliente(models.Model):
	nombre    = models.CharField(max_length=100)
	apellido  = models.CharField(max_length=100)
	celular   = models.BigIntegerField()


	def get_abosulte_url(self):
		return reverse('cliente-detalle', args=[str(self.id)])


	def __str__(self):
		   return '{0} {1}'.format(
			   self.nombre, self.apellido)

class Orden(models.Model):

	pass

	"""def getTotal(self):
		return sum(self.renta.getSubtotal() * self.renta)

	def __str__(self):
		return 'Cliente {0} {1}'.format(
									self.propietario.nombre, self.propietario.apellido)
									#self.getTotal())

	def get_absolute_url(self):
		return reverse('cliente-detalle', args=[str(self.id)])
"""

class Pedido(models.Model):
	propietario = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID de la orden")
	renta = models.ForeignKey('Renta', on_delete=models.SET_NULL, null=True)
	observacion = models.TextField(help_text="Observacion Adicional", blank=True)

	date_deliver = models.DateField("Fecha de entrega", null=True, blank=True, help_text="Fecha en que se entregara el pedido")
	date_receive = models.DateField("Fecha de retorno", null=True, blank=True, help_text="Fecha en que se debe recibir el pedido")
	date_return = models.DateField("Fecha de devolucion", null=True, blank=True, help_text="Fecha en que el cliente devolvio el pedido")

	PAGADO             = 'P'
	PENDIENTE          = 'PP'
	ENTREGADO          = 'E'
	ALQUILADO          = 'A'
	ALQUILER_PENDIENTE = 'AP'
	LOCAL              = 'L'
	ENTREGAR           = 'EE'

	PAY     = ((PAGADO, 'Pagado'),(PENDIENTE,'Pendiente Pago'),)
	RENT    = ((ENTREGADO, 'Entregado'), (ALQUILADO, 'En Alquiler'), (ALQUILER_PENDIENTE,'Alquiler Pendiente'),)
	DELIVER = ((LOCAL, 'Local'),(ENTREGAR,'Entrega exterior'),)

	estado_de_Pago  = models.CharField(max_length=2, choices=PAY, default=PAGADO)
	pago_pendiente  = models.PositiveIntegerField(blank=True)
	deposito        = models.PositiveIntegerField(blank=True)
	estado_de_renta = models.CharField(max_length=2, choices=RENT, default=ALQUILADO)
	tipo_de_entrega = models.CharField(max_length=2, choices=DELIVER, default=LOCAL)
	direccion       = models.TextField(help_text='Solo en caso de entrega exterior', blank=True)


	class Meta:
		ordering = ["date_deliver"]


	def __str__(self):
		return '%s' % (self.estado_de_renta)
