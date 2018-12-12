from django.db import models
from datetime import date

class Cliente(models.Model):
	nombre    = models.CharField(max_length=50)
	apellido  = models.CharField(max_length=50)
	direccion = models.TextField()
	celular   = models.PositiveIntegerField()
	created_at= models.DateTimeField(auto_now_add=True)
	Orden     = models.TextField()
	Total_Lps = models.PositiveIntegerField()
	deposito  = models.PositiveIntegerField()

	
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
	Estado_de_Pago     = models.CharField(max_length=2, choices=PAY, default=PAGADO)
	Pago_pendiente = models.PositiveIntegerField()
	Estado_de_Renta    = models.CharField(max_length=2, choices=RENT, default=ALQUILADO)
        Tipo_de_Entrega = models.CharField(max_length=2, choices=DELIVER, default=LOCAL)

	def __str__(self):
		   return '{} {} ({})'.format(
			   self.nombre, self.apellido, self.Estado_de_Renta)
