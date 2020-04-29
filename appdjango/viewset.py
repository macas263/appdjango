from rest_framework import viewsets
from .models import *
from .serializer import *



class VendedorViewset(viewsets.ModelViewSet):
	queryset = Vendedor.objects.all()
	serializer_class = VendedorSerializer


class CompradorViewset(viewsets.ModelViewSet):
	queryset = Comprador.objects.all()
	serializer_class = CompradorSerializer




class ArticuloViewset(viewsets.ModelViewSet):
	queryset = Articulo.objects.all()
	serializer_class = ArticuloSerializer


class EnvioViewset(viewsets.ModelViewSet):
	queryset = Envio.objects.all()
	serializer_class = EnvioSerializer





class RegistroViewset(viewsets.ModelViewSet):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer