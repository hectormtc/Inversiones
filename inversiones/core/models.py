from django.db import models

class Client(models.Model):
	fname   = models.CharField(max_length=50)
	lnmae   = models.CharField(max_length=50)
	address = models.TextField()
	phone   = models.PositiveIntegerField()
	deposit = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	date       = models.DateTimeField(default=datetime.now, blank=True)
	order      = models.TextField()

	
	PAGADO             = 'P'
	PENDIENTE          = 'PP'
	ENTREGADO          = 'E'
	ALQUILADO          = 'A'
	ALQUILER_PENDIENTE = 'AP'
	LOCAL              = 'L'
	ENTREGAR           = 'EE'
	
	PAY     = (('PAGO', (
		  (PAGADO, 'Pagado'),
		  (PENDIENTE,'Pendiente Pago'),)
	RENT    = (('ESTADO', (
		  (ENTREGADO, 'Entregado'),
		  (ALQUILADO, 'En Alquiler'),
		  (ALQUILER_PENDIENTE,'Alquiler Pendiente'),)
	DELIVER = ('ENTREGA', (
		  (LOCAL, 'Local'),
		  (ENTREGAR,'Entrega exterior'),)
		 
	state_pay     = models.CharField(max_length=2, choices=PAY, default=PAGADO)
	state_rent    = models.CharField(max_length=2, choices=RENT, default=ALQUILADO)
        state_deliver = models.CharField(max_lenght=2, choices=DELIVER, default=LOCAL)

	def __str__(self):
		   return '{} {} - {}'.format(
			   self.fname, self.lname, state_rent)
