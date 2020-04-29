from django.db import models


# Create your models here.

def url_articulo(self, filename):
	ruta = "static/fotos/lugares/%s%s"%(self.nombre, str(filename))
	return ruta


class Envio(models.Model):
	fecha_envio = models.DateField()
	direccion_envio = models.CharField(max_length=50)
	
	def __str__(self):
		return self.direccion_envio 



 



class Vendedor(models.Model):
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=40)
	direccion =  models.CharField(max_length=40)
	correo =  models.CharField(max_length=40)
	telefono =  models.CharField(max_length=10)

	
	def __str__(self):
		return self.nombre




class Articulo(models.Model):
	def foto_art(self):
		return mark_safe('<a href="/%s"> <img heigth="120px" width="120px" src=/%s> </a>'%(self.foto_articulo, self.foto_articulo))

	nombre = models.CharField(max_length=35)
	descripcion = models.TextField(max_length=100)
	precio = models.DecimalField(decimal_places = 1, max_digits=5)
	fk_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
	foto_articulo  = models.ImageField(upload_to=url_articulo)

	def __str__(self):
		return self.descripcion


class Comprador(models.Model):
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=35)
	direccion = models.CharField(max_length=35)
	correo =  models.CharField(max_length=40)
	telefono =  models.CharField(max_length=10)
	fk_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.nombre


class Registro(models.Model):
	fechapago = models.DateField()
	detallepago = models.CharField(max_length=45)

	def __str__(self):
		return self.detallepago
