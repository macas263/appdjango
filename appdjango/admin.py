from django.contrib import admin
from .models import * 

# Register your models here.



# Register your models here.


class ArticuloAdmin(admin.ModelAdmin):
	list_dislplay = ('nombre', 'descripcion', 'precio', 'fk_vendedor', 'foto_articulo')
admin.site.register(Articulo, ArticuloAdmin)

class CompradorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'direccion', 'correo', 'telefono', 'fk_articulo')
admin.site.register(Comprador, CompradorAdmin)

class VendedorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'direccion', 'correo', 'telefono')
admin.site.register(Vendedor, VendedorAdmin)


class EnvioAdmin(admin.ModelAdmin):
	list_display = ('fecha_envio', 'direccion_envio')
admin.site.register(Envio, EnvioAdmin) 


class RegistroAdmin(admin.ModelAdmin):
	list_display = ('fechapago', 'detallepago')
admin.site.register(Registro, RegistroAdmin)

