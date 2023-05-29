from django.urls import path
from . import views

urlpatterns = [
    # Ruta de la página de inicio
    path('', views.index, name='index'),
    path('empleados/nuevo',views.registrar_empleado,name="registrar_empleado"),
    path('empleados/listado/', views.listar_empleados, name='listar_empleados'),
    path('empleados/activar/<int:id>', views.activar_registro_empleado, name="activar_registro_empleado"),
    path('empleados/actualizar/<int:id_empleado>', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado, name='desactivar_empleado'),
    path('coordinadores/nuevo', views.registrar_coordinador,name='registrar_coordinador'),
    path('coordinadores/listado/', views.listar_coordinadores, name='listar_coordinadores'),
    path('coordinadores/actualizar/<int:id_coordinador>', views.actualizar_coordinador, name='actualizar_coordinador'),
    path('clientes/nuevo/', views.registrar_cliente, name='registrar_cliente'),
    path('clientes/activar/<int:id_cliente>', views.activar_cliente, name='activar_cliente'),
    path('clientes/desactivar/<int:id_cliente>', views.desactivar_cliente, name='desactivar_cliente'),
    path('clientes/eliminar/<int:id_cliente>', views.eliminar_cliente, name='eliminar_cliente'),
    path('coordinadores/activar/<int:id_coordinador>', views.activar_coordinador, name='activar_coordinador'),
    path('coordinadores/desactivar/<int:id_coordinador>', views.desactivar_coordinador, name='desactivar_coordinador'),
    path('clientes/actualizar/<int:id_cliente>', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/listado/', views.listar_clientes, name='listar_clientes'),
]
