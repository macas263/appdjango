"""tendencias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appdjango import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio_view, name='vista_inicio'),
    path('articulos/', views.lista_articulos, name='vista_articulo'),
    path('envios/', views.lista_envios, name='vista_envio'),
    path('vendedores/', views.lista_vendedores, name='vista_vendedor'),
    path('compradores/', views.lista_compradores, name='vista_compradores'), 
    path('registros/', views.lista_registro, name='vista_registro'),

   
    #url articulo
    
    path('editar/<id>/', views.EditarArticulo, name='vista_articulo'),
    path('añadir/articulo/', views.Añadir_Articulo, name='nuevo_articulo'),
    path('eliminar/<id>/', views.Eliminar_Articulo, name='delete_articulo'),


    path('editarr/<id>/', views.EditarRegistro, name='vista_registro'),
    path('añadir/registro/', views.Añadir_Registro, name='nuevo_registro'),
    path('eliminarr/<id>/', views.Eliminar_Registro, name='delete_registro'),

    #url comprador
    path('editarc/<id>/', views.EditarComprador, name='editar_comprador'),
    path('añadir/comprador/', views.Añadir_Comprador, name='nuevo_comprador'),
    path('eliminarc/<id>/', views.Eliminar_Comprador, name='delete_comprador'),

    #url vendedor
    path('editarv/<id>/', views.EditarVendedor, name='editar_vendedor'),
    path('añadir/vendedor/', views.Añadir_Vendedor, name='nuevo_vendedor'),
    path('eliminarv/<id>/', views.Eliminar_Vendedor, name='delete_vendedor'),

    #url envios
    path('editare/<id>/', views.EditarEnvio, name='editar_envio'),
    path('añadir/envio/', views.Añadir_Envio, name='nuevo_envio'),
    path('eliminare/<id>/', views.Eliminar_Envio, name='delete_envio'),

    path('api/v1.0/', include('appdjango.urls')),
    path('api/v1.0/', include('appdjango.urls')),
    path('api/v1.0/', include('appdjango.urls')),
    path('api/v1.0/', include('appdjango.urls')),
    path('api/v1.0/', include('appdjango.urls')),

]
