from django.db import models
from datetime import date
from django.urls import reverse
import uuid


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


class Categoria(models.Model):
	categoria = models.CharField(max_length=50, help_text="Tipo de categoria")

	def __str__(self):
		return self.categoria	


class Producto(models.Model):
	producto  = models.CharField(max_length=200, help_text="Nombre del producto")
	detalles  = models.TextField(help_text="Detalles sobre el producto")
	precio    = models.PositiveIntegerField()
	cantidad  = models.PositiveIntegerField()
	categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return '{} {}'.format(
			self.producto, self.detalles)


class Orden(models.Model):
        propietario = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
	observacion = models.TextField(help_text="Observacion Adicional")
	direccion   = models.TextField()

	producto = models.ManyToManyField(Producto, help_text="Ingrese el alquiler")

	deposito  = models.PositiveIntegerField()
	Total_Lps = models.PositiveIntegerField()

	

	def __str__(self):
            return self.propietario

	def get_absolute_url(self):
            return reverse('cliente-detalle', args=[str(self.id)])


class Pedido(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID de la orden")
	orden = models.ForeignKey('Orden', on_delete_models.SET_NULL, null=True)

	date_deliver = models.DateField("Fecha de entrega", null=True, blank=True, help_text="Fecha en que se entregara el pedido")
	date_receive = models.DateField("Fecha de retorno", null=True, blank=True, help_text="Fecha en que se debe recibir el pedido)
	date_return = models.DateField("Fecha de devolucion", null=True, blank=True, help_text="Fecha en que el cliente devolvio el pedido")

	entrega = models.ManyToManyField(Entrega, help_text="Tipo de Entrega")
	estado  = models.ManyToManyField(Estado, help_text="Estado de Alquiler")
	pago    = models.ManyToManyField(Pago, help_text="Estado de Pago")

	class Meta:
		ordering = ["date_deliver"]

	def __str__(self):
		return '%s (%s)' % (self.id, self.


class Cliente(models.Model):
	nombre    = models.CharField(max_length=100)
	apellido  = models.CharField(max_length=100)
	celular   = models.PositiveIntegerField()

	def __str__(self):
		   return '{} {}'.format(
			   self.nombre, self.apellido)
	
	def get_abosulte_url(self):
		return reverse('cliente-detalle', args=[str(self.id)])
	
	
