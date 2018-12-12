from django.db import models
from datetime import date
from django.urls import reverse
import uuid

"""
class Pago(models.Model):
	pago = models.CharField(max_length=200, help_text="Especifique un tipo de pago")

	def __str__(self):
		return self.pago


class Estado(models.Model):
	estado = models.CharField(max_length=200, help_text="Especifique de estado de renta")

	def __str__(self):
		return self.estado


class Entrega(models.Model):
	entrega = models.CharField(max_length=200, help_text="Especifique el tipo de entrega")

	def __str__(self):
		return self.entrega
"""

class Categoria(models.Model):
	categoria = models.CharField(max_length=50, help_text="Tipo de categoria")

	def __str__(self):
            return self.categoria


class Producto(models.Model):
	producto  = models.CharField(max_length=200, help_text="Nombre del producto")
	detalles  = models.TextField(help_text="Detalles sobre el producto")
	precio    = models.PositiveIntegerField()
	cantidad  = models.PositiveIntegerField()
	categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return '{} {}'.format(self.producto, self.detalles)


class Orden(models.Model):
	propietario = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
	observacion = models.TextField(help_text="Observacion Adicional")
	direccion   = models.TextField()
	producto = models.ManyToManyField(Producto, help_text="Ingrese el alquiler")
	deposito  = models.PositiveIntegerField()
	total = models.PositiveIntegerField('Total Lps')

	def __str__(self):
		return self.propietario.nombre

	def get_absolute_url(self):
		return reverse('cliente-detalle', args=[str(self.id)])


class Pedido(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID de la orden")
	orden = models.ForeignKey('Orden', on_delete=models.SET_NULL, null=True)

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
	pago_pendiente  = models.PositiveIntegerField()
	estado_de_renta = models.CharField(max_length=2, choices=RENT, default=ALQUILADO)
	tipo_de_entrega = models.CharField(max_length=2, choices=DELIVER, default=LOCAL)


	class Meta:
		ordering = ["date_deliver"]


	def __str__(self):
		return '%s (%s)' % (self.orden.propietario.nombre, self.estado_de_renta)


class Cliente(models.Model):
	nombre    = models.CharField(max_length=100)
	apellido  = models.CharField(max_length=100)
	celular   = models.PositiveIntegerField()


	def get_abosulte_url(self):
		return reverse('cliente-detalle', args=[str(self.id)])


	def __str__(self):
		   return '{} {}'.format(
			   self.nombre, self.apellido)
