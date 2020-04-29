from .models import *
from django import forms
from django.contrib.admin import widgets





class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo
		fields = '__all__'



class CompradorForm(forms.ModelForm):
	class Meta:
		model = Comprador
		fields = '__all__'



class RegistroForm(forms.ModelForm):
	class Meta:
		model = Registro
		fields = '__all__'





class EnvioForm(forms.ModelForm):
	class Meta:
		model = Envio
		fields = '__all__'

class VendedorForm(forms.ModelForm):
	class Meta:
		model = Vendedor
		fields = '__all__'


