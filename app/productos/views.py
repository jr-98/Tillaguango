from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormularioProductos
from django.contrib.auth.decorators import login_required
from app.modelo.models import Producto
from django.views.generic import TemplateView 

def principal(request):
	lista = Producto.objects.all()
	context = {
		'lista': lista,
	}
	return render(request,'producto/principal_producto.html',context)
	#return HttpResponse('ES el index del cliente')
def crear(request):
	formulario = FormularioProductos(request.POST)
	if request.method =='POST':
		if formulario.is_valid():
			datos = formulario.cleaned_data
			Productos = Producto()
			Productos.idt = datos.get('idt')
			Productos.nombre = datos.get('nombre')
			Productos.modelo = datos.get('modelo')
			Productos.marca = datos.get('marca')
			Productos.precio = datos.get('precio')
			Productos.fechaIngreso = datos.get('fechaIngreso')
			Productos.descripcion= datos.get('descripcion')
			Productos.save()
			return redirect(principal)
	context = {
		'f': formulario
	}
	return render (request,'producto/crear_producto.html',context)
    #return HttpResponse('Esta es la interfaz que atendera su funcion de crear clientes')






