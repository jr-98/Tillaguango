from django.contrib import admin
from .models import Producto

class AdminProductos(admin.ModelAdmin):
	list_display = ["idt","nombre","modelo","marca","precio","fechaIngreso","descripcion"]
	list_editable = ["nombre","marca","precio","descripcion"]
	list_filter = ["idt","modelo","nombre","marca","precio"]
	search_fiels = ["idt","modelo","nombre","marca","precio"]

	class Meta:
		model = Producto

admin.site.register(Producto, AdminProductos)

