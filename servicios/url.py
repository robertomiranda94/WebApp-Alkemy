from django.urls import path
from . import views

urlpatterns = [
    # Ruta de la página de inicio
    path('', views.index, name='index'),
    path('empleados/nuevo',views.registrar_empleado,name="registrar_empleado"),
    path('empleados/activar/<int:id>', views.activar_registro_empleado, name="activar_registro_empleado"),
    path('empleados/actualizar/<int:id_empleado>', views.actualizar_empleado, name='actualizar_empleado')
]
