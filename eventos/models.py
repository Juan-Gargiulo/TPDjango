from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''
Modelos:
Evento= descripcion, fecha, publicidad (imagen), espacio
Espacio= ciudad, domicilio, nombre
Sector=nombre, cantidad_lugares, precio, espacio
Lugar= numero, sector, evento
Entrada= numero_tkt, lugar
'''


class Espacio(models.Model):
	ciudad = models.CharField(max_length=50)
	domicilio = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural='Espacios'

	def __str__(self):
		return self.nombre

class Evento(models.Model):
	descripcion = models.CharField(max_length=50)
	fecha = models.DateField()
	publicidad = models.ImageField()
	espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural='Eventos'

	def __str__(self):
		return self.descripcion

class Sector(models.Model):
	mombre = models.CharField(max_length=50)
	cantidad_lugares = models.IntegerField()
	precio = models.DecimalField(max_digits=5,decimal_places=2)
	espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


class Lugar(models.Model):
	numero = models.IntegerField()
	sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class Entrada(models.Model):
	numero_tkt = models.IntegerField()
	lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

	def __str__(self):
		return self.numero_tkt
