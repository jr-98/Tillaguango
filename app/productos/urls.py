from django.urls import path
from . import views

urlpatterns=[
	path('',views.principal, name='productos'),
	path('crear', views.crear),
]
