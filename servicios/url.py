from django.urls import path
from . import views
from .views import nuevo_coordinador

urlpatterns = [
    # Ruta de la página de inicio
    path('', views.index, name='index'),
    path('empleados/nuevo',views.registrar_empleado,name="registrar_empleado"),
    path('empleados/listado/', views.listar_empleados, name='listar_empleados'),
    path('empleados/activar/<int:id>', views.activar_registro_empleado, name="activar_registro_empleado"),
    path('empleados/actualizar/<int:id_empleado>', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado, name='desactivar_empleado'),
    path('coordinadores/listado/', views.listar_coordinadores, name='listar_coordinadores'),
    path('coordinadores/actualizar/<int:id_coordinador>', views.actualizar_coordinador, name='actualizar_coordinador'),
    path('clientes/nuevo/', views.registrar_cliente, name='registrar_cliente'),
    path('clientes/activar/<int:id_cliente>', views.activar_cliente, name='activar_cliente'),
    path('clientes/desactivar/<int:id_cliente>', views.desactivar_cliente, name='desactivar_cliente'),
    path('coordinadores/nuevo', views.nuevo_coordinador, name='nuevo_coordinador'),
]
