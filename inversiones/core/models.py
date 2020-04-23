# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.urls import reverse

class Address(models.Model):
    address = models.CharField(
                            max_length=50
                            )
    def __str__(self):
            return self.address



class Producto(models.Model):
    producto  = models.CharField('Producto', max_length=200, help_text="Nombre del producto")
    detalles  = models.CharField(max_length=200, help_text="Detalles sobre el producto",blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    precio    = models.PositiveIntegerField()
    cantidad  = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)


    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

    def display_Categoria(self):
        return ', '.join([ self.categoria.categoria])
        display_Categoria.short_description = 'Categoria'

    def __str__(self):
        return '{0} {1}'.format(self.producto, self.detalles)

    def get_absolute_url(self):
        return reverse('producto_detalle',
                        args=[self.id, self.slug])


class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Encargado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    rol = models.ForeignKey(
                            'Rol',
                            on_delete=models.CASCADE,
                            null=True
                            )
    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellido)



class Categoria(models.Model):
    categoria = models.CharField(
                            max_length=50,
                            help_text="Tipo de categoria"
                            )
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('categoria',)
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
                    return self.categoria

    def get_abosulte_url(self):
        return reverse('core:producto_lista_por_categoria',
                        args=[self.slug])

class Inventario(models.Model):
    producto  = models.CharField(
                                'Producto',
                                max_length=200,
                                help_text="Nombre del producto"
                                )
    detalles  = models.CharField(
                                max_length=200,
                                help_text="Detalles sobre el producto",
                                blank=True
                                )
    cantidad  = models.PositiveIntegerField()
    precio    = models.PositiveIntegerField()
    categoria = models.ForeignKey(
                                'Categoria',
                                on_delete=models.CASCADE,
                                null=True
                                )

    def display_Categoria(self):
            return ', '.join([ self.categoria.categoria])
            display_Categoria.short_description = 'Categoria'

    class Meta:
        ordering = ('producto',)
        index_together = (('id', 'detalles'))

    def __str__(self):
            return '{0},  {1},Precio: {2}, Inventario: {3}'.format(
                                            self.producto,
                                            self.detalles,
                                            self.precio,
                                            self.cantidad
                                            )


class Articulo(models.Model):
    producto = models.ForeignKey('Producto',on_delete=models.CASCADE,null=False)
    cantidad  = models.PositiveIntegerField()
    #producto = models.ManyToManyField(Inventario)


    def getProductName(self):
        return '%s %s' % (
                        self.producto.producto,
                        self.producto.detalles
                        )


    def getSubtotal(self):
            return int(
                    self.producto.precio * self.cantidad
                    )

    def getTotal(self):
            return sum(self.getSubtotal())

    def __str__(self):
            return '{0}, Cantidad: {1}, SubTotal: {2}'.format(
                                            self.producto,
                                            self.cantidad,
                                            self.getSubtotal()
                                            )

class ArticuloInstance(models.Model):
    #producto = models.ManyToManyField(Inventario)
    #cantidad  = models.PositiveIntegerField()
    articulo = models.ForeignKey('Articulo', on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey('Producto',on_delete=models.CASCADE,null=False)
    cantidad  = models.PositiveIntegerField()

    def getSubtotal(self):
            return int(
                    self.producto.precio * self.cantidad
                    )

    def getTotal(self):
            return sum(self.getSubtotal())

    def __str__(self):
            return '{0}, Cantidad: {1}, SubTotal: {2}'.format(
                                            self.articulo,
                                            self.cantidad,
                                            self.getSubtotal()
                                            )


class Orden(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para esta factura",editable=False)
    #articulo = models.ForeignKey('Articulo', on_delete=models.CASCADE,null=True)
    articulo = models.ManyToManyField(Articulo)
    total = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return 'Orden: %s ' % (
                            self.id# .getProductName()
                            )


import uuid

class Factura(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para esta factura", editable=False)

    client = models.ForeignKey(
                                'Cliente',
                                on_delete=models.SET_NULL,
                                null=True
                                )
    #orden = models.ForeignKey('Orden', on_delete=models.SET_NULL,null=True)
    encargado = models.ForeignKey(
                                'Encargado',
                                on_delete=models.SET_NULL,
                                null=True
                                )

    orden = models.ForeignKey('Orden',
                              on_delete=models.SET_NULL,
                              null=True)


    PAGADO             = 'P'
    PENDIENTE          = 'PP'
    ENTREGADO          = 'E'
    ALQUILADO          = 'A'
    ALQUILER_PENDIENTE = 'AP'
    LOCAL              = 'L'
    ENTREGAR           = 'EE'

    PAY     = (
            (PAGADO, 'Pagado'),
            (PENDIENTE,'Pendiente Pago'),
            )
    RENT    =((ENTREGADO, 'Entregado'),
            (ALQUILADO, 'En Alquiler'),
            (ALQUILER_PENDIENTE,'Alquiler Pendiente'),
            )
    DELIVER = ((LOCAL, 'Local'),
            (ENTREGAR,'Entrega exterior'),
            )

    estado_de_pago  = models.CharField(max_length=2,choices=PAY, default=PAGADO)
    estado_de_renta = models.CharField(max_length=2, choices=RENT, default=ALQUILADO)
    tipo_de_entrega = models.CharField(max_length=2, choices=DELIVER, default=LOCAL)
    pago_pendiente  = models.PositiveIntegerField(blank=True, null=True)
    deposito        = models.PositiveIntegerField(blank=True, null=True)
    direccion       = models.CharField(max_length=100, help_text='Solo en caso de entrega exterior', blank=True)
    observacion     = models.CharField(max_length=100, help_text="Observacion Adicional", blank=True)
    date_deliver = models.DateField("Fecha de entrega", null=True, blank=True, help_text="Fecha en que se entregara el pedido")
    date_receive = models.DateField("Fecha de retorno", null=True, blank=True, help_text="Fecha en que se debe recibir el pedido")

    class Meta:
        ordering = ["date_deliver", "date_receive"]

    def __str__(self):
        return '{0} ({1})'.format(self.client, self.orden)


class Cliente(models.Model):
    nombre    = models.CharField(max_length=100)
    apellido  = models.CharField(max_length=100, blank=True)
    empresa   = models.BooleanField()
    #date = models.DateTimeField(auto_now_add=True,null=True)
    phone = models.PositiveIntegerField()
    #facturacion = models.ManyToManyField('FacturaInstance', blank=True)
    #facturacion = models.ForeignKey('Factura', on_delete=models.SET_NULL,null=True)

    #def get_abosulte_url(self):
    #    return reverse('cliente-detalle', args=[str(self.id)])


    def __str__(self):
           return '{0} {1}'.format(self.nombre, self.apellido)

    def get_absolute_url(self):
        return reverse('client-detail/', args=[str(self.id)])

class Historial(models.Model):
    cliente = models.ForeignKey('Cliente',on_delete=models.SET_NULL,
    null=True)
    factura = models.ForeignKey('Factura',on_delete=models.SET_NULL,
    null=True)
