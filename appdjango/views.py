from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponseRedirect


# Create your views here.

def inicio_view(request):
    usuario = request.user
    return render(request, 'inicio.html', {'usuario': usuario})
    
def lista_envios(request):
	envios = Envio.objects.all()
	ctx = {'envios':envios}
	return render(request, 'lista_envios.html', ctx)

def lista_compradores(request):
	compradores = Comprador.objects.all()
	ctx = {'compradores':compradores}
	return render(request, 'lista_compradores.html', ctx)

def lista_vendedores(request):
	vendedores = Vendedor.objects.all()
	ctx = {'vendedores':vendedores}
	return render(request, 'lista_vendedores.html', ctx)

def lista_articulos(request):
	articulos = Articulo.objects.all()
	ctx = {'articulos':articulos}
	return render(request, 'lista_articulos.html', ctx)

def lista_registro(request):
	registros = Registro.objects.all()
	ctx = {'registros':registros}
	return render(request, 'lista_registro.html', ctx)



def EditarArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articulos/')
        else:
            form = ArticuloForm(instance=articulo)
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'editar_articulo.html', {'articulo':articulo, 'form':form})



def Añadir_Articulo(request):
	if request.method == 'POST':
		form = ArticuloForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'nuevo_articulo.html',{'info':"Guardado correctamente"})
	
	else: 
		form = ArticuloForm()
	return render(request, 'nuevo_articulo.html', {'form' :form})
			

def Eliminar_Articulo(request, id):
	articulo = Articulo.objects.get(id=id)
	if request.method == 'POST':
		articulo.delete()
		return HttpResponseRedirect('/articulos/')
	return render(request, 'eliminar_articulo.html', {'articulo':articulo})

#COMPRADOR-------------------------------------------------------------------------------------

def EditarComprador(request, id):
    comprador = Comprador.objects.get(id=id)
    if request.method == 'POST':
        form = CompradorForm(request.POST, request.FILES, instance=comprador)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/compradores/')
        else:
            form = CompradorForm(instance=comprador)
    else:
        form = CompradorForm(instance=comprador)
    return render(request, 'editar_comprador.html', {'comprador':comprador, 'form':form})



def Añadir_Comprador(request):
	if request.method == 'POST':
		form = CompradorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'nuevo_comprador.html',{'info':"Guardado correctamente"})
	
	else: 
		form = CompradorForm()
	return render(request, 'nuevo_comprador.html', {'form' :form})
			

def Eliminar_Comprador(request, id):
	comprador = Comprador.objects.get(id=id)
	if request.method == 'POST':
		comprador.delete()
		return HttpResponseRedirect('/compradores/')
	return render(request, 'eliminar_comprador.html', {'comprador':comprador})

# REGISTRO
def EditarRegistro(request, id):
    registro = Registro.objects.get(id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES, instance=registro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registros/')
        else:
            form = RegistroForm(instance=registro)
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'editar_registro.html', {'registro':registro, 'form':form})



def Añadir_Registro(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'nuevo_registro.html',{'info':"Guardado correctamente"})
	
	else: 
		form = RegistroForm()
	return render(request, 'nuevo_registro.html', {'form' :form})
			

def Eliminar_Registro(request, id):
	registro = Registro.objects.get(id=id)
	if request.method == 'POST':
		registro.delete()
		return HttpResponseRedirect('/registros/')
	return render(request, 'eliminar_registro.html', {'registro':registro})

#Vendedor--------------------------------------------------------------------------------------

def EditarVendedor(request, id):
    vendedor = Vendedor.objects.get(id=id)
    if request.method == 'POST':
        form = VendedorForm(request.POST, request.FILES, instance=vendedor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vendedores/')
        else:
            form = VendedorForm(instance=vendedor)
    else:
        form = VendedorForm(instance=vendedor)
    return render(request, 'editar_vendedor.html', {'vendedor':vendedor, 'form':form})



def Añadir_Vendedor(request):
	if request.method == 'POST':
		form = VendedorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'nuevo_vendedor.html', {'info':"Guardado correctamente"})
	
	else: 
		form = VendedorForm()
	return render(request, 'nuevo_vendedor.html', {'form' :form})
			

def Eliminar_Vendedor(request, id):
	vendedor = Vendedor.objects.get(id=id)
	if request.method == 'POST':
		vendedor.delete()
		return HttpResponseRedirect('/vendedores/')
	return render(request, 'eliminar_vendedor.html', {'vendedor':vendedor})	


# EnviooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooivnE

def EditarEnvio(request, id):
    envio = Envio.objects.get(id=id)
    if request.method == 'POST':
        form = EnvioForm(request.POST, request.FILES, instance=envio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/envios/')
        else:
            form = EnvioForm(instance=envio)
    else:
        form = EnvioForm(instance=envio)
    return render(request, 'editar_envio.html', {'envio':envio, 'form':form})



def Añadir_Envio(request):
	if request.method == 'POST':
		form = EnvioForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'nuevo_envio.html', {'info':"Guardado correctamente"})
	
	else: 
		form = EnvioForm()
	return render(request, 'nuevo_envio.html', {'form' :form})
			

def Eliminar_Envio(request, id):
	envio = Envio.objects.get(id=id)
	if request.method == 'POST':
		envio.delete()
		return HttpResponseRedirect('/envios/')
	return render(request, 'eliminar_envio.html', {'envio':envio})
