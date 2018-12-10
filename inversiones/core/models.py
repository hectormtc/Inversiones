from django.db import models

class Client(models.Model):

	fname = models.CharField(max_length=50)