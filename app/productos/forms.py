from django import forms
from app.modelo.models import Producto

class FormularioProductos(forms.ModelForm):
	class  Meta:
		model = Producto
		fields = ["idt","nombre","modelo","marca","precio","fechaIngreso","descripcion"]