from rest_framework import serializers
from .models import *





class VendedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vendedor
		fields = '__all__' 




class CompradorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comprador
		fields = '__all__'



class ArticuloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articulo
		fields = '__all__' 




class EnvioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Envio
		fields = '__all__'




class RegistroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registro
		fields = '__all__'