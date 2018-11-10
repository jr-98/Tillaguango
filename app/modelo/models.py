from django.db import models

class Producto(models.Model):
	idt = models.CharField('ID', max_length = 10, unique = True)
	nombre = models.CharField('Nombre', max_length = 50, unique = True)
	modelo = models.CharField('Modelo', max_length = 50, blank=False, null = False)
	marca = models.CharField('Marca', max_length = 25, blank = False, null = False)
	precio = models.DecimalField(max_digits=7,decimal_places=2)
	fechaIngreso = models.DateField()
	descripcion=models.TextField(max_length=30)

	def getCaracteristicas(self):
		cadena = '{0} {1} {2}'
		return cadena.format(self.nombre, self.modelo, self.precio)

	def __str__(self):
		return self.idt


	