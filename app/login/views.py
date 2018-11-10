

from django.shortcuts import render
from .forms import formularioLogin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def loginPage (request):
	
	if request.method =='POST':
		
		formulario = formularioLogin(request.POST)
		if formulario.is_valid():
			usuario = request.POST["username"]
			clave = request.POST["password"]
			user = authenticate(username=usuario, password=clave)
			if user is not None:
				if user.is_active:
					login(request, user)
					#messages.warning(request,'Te has logeado de forma correcta')
					#return HttpResponse('lklkv')
					return HttpResponseRedirect(reverse('productos'))
				else:
					messages.warning(request,'usuario inactivo')
			else:
				messages.warning(request,'Usuario o password es incorrecto')
	else:
		formulario = formularioLogin()
	context = {
		'f':formulario,
		}
	return render(request,'login/login.html', context)

def logoutPage(request):
	logout(request)
	return HttpResponseRedirect(reverse('home_Page'))
