from django.urls import path
from . import views

urlpatterns = [
    # Ruta de la página de inicio
    path('', views.index, name='index'),
    path('empleados/nuevo',views.registrar_empleado,name="registrar_empleado")
]
