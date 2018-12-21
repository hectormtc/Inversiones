# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.urls import reverse

class Categoria(models.Model):
	categoria = models.CharField(max_length=50, help_text="Tipo de categoria")

	def __str__(self):
            return self.categoria


class Producto(models.Model):
	producto  = models.CharField('Producto', max_length=200, help_text="Nombre del producto")
	detalles  = models.CharField(max_length=200, help_text="Detalles sobre el producto",blank=True)
	precio    = models.PositiveIntegerField()
	cantidad  = models.PositiveIntegerField()
	categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

	def display_Categoria(self):
		return ', '.join([ self.categoria.categoria])
		display_Categoria.short_description = 'Categoria'

	def __str__(self):
		return '{0} {1}'.format(self.producto, self.detalles)

class Renta(models.Model):
	producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
	cantidad = models.PositiveIntegerField()

	def getSubtotal(self):
		return int(self.cantidad * self.producto.precio)

	def __str__(self):
		return 'Producto: {0}, Cantidad: {1} Subtotal: {2}'.format(self.producto,self.cantidad,self.getSubtotal())

import uuid

class Pedido(models.Model):
	cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
	#renta = models.ForeignKey('Renta', on_delete=models.SET_NULL, null=True)
	#renta = models.ManyToManyField(Renta, through='Cliente')

	date_deliver = models.DateField("Fecha de entrega", null=True, blank=True, help_text="Fecha en que se entregara el pedido")
	date_receive = models.DateField("Fecha de retorno", null=True, blank=True, help_text="Fecha en que se debe recibir el pedido")
	date_return  = models.DateField("Fecha de devolucion", null=True, blank=True, help_text="Fecha en que el cliente devolvio el pedido")

	PAGADO             = 'P'
	PENDIENTE          = 'PP'
	ENTREGADO          = 'E'
	ALQUILADO          = 'A'
	ALQUILER_PENDIENTE = 'AP'
	LOCAL              = 'L'
	ENTREGAR           = 'EE'

	PAY     = ((PAGADO, 'Pagado'),(PENDIENTE,'Pendiente Pago'),)
	RENT    = ((ENTREGADO, 'Entregado'),(ALQUILADO, 'En Alquiler'), (ALQUILER_PENDIENTE,'Alquiler Pendiente'),)
	DELIVER = ((LOCAL, 'Local'),(ENTREGAR,'Entrega exterior'),)

	estado_de_pago  = models.CharField(max_length=2,choices=PAY, default=PAGADO)
	estado_de_renta = models.CharField(max_length=2, choices=RENT, default=ALQUILADO)
	tipo_de_entrega = models.CharField(max_length=2, choices=DELIVER, default=LOCAL)
	pago_pendiente  = models.PositiveIntegerField(blank=True)
	deposito        = models.PositiveIntegerField(blank=True)
	direccion       = models.TextField(help_text='Solo en caso de entrega exterior', blank=True)
	observacion     = models.TextField(help_text="Observacion Adicional", blank=True)


	class Meta:
		ordering = ["date_deliver"]


	def __str__(self):
		return '%s' % (self.cliente.nombre)

class Cliente(models.Model):
	nombre    = models.CharField(max_length=100)
	apellido  = models.CharField(max_length=100, blank=True)
	celular   = models.BigIntegerField()
	empresa   = models.BooleanField()
	#rentas    = models.ManyToManyField(Pedido)


	def get_abosulte_url(self):
		return reverse('cliente-detalle', args=[str(self.id)])


	def __str__(self):
		   return '{0} {1}'.format(self.nombre, self.apellido)
