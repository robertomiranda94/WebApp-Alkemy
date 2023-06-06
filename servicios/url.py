from django.urls import path
from . import views

urlpatterns = [

    # EMPLEADOS
    path('', views.index, name='index'),
    path('empleados/nuevo',views.registrar_empleado,name="registrar_empleado"),
    path('empleados/listado/', views.listar_empleados, name='listar_empleados'),
    path('empleados/activar/<int:id>', views.activar_empleado, name="activar_empleado"),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado, name='desactivar_empleado'),
    path('empleados/actualizar/<int:id_empleado>', views.actualizar_empleado, name='actualizar_empleado'),
    # COORDINADORES
    path('coordinadores/nuevo', views.registrar_coordinador,name='registrar_coordinador'),
    path('coordinadores/listado/', views.listar_coordinadores, name='listar_coordinadores'),
    path('coordinadores/activar/<int:id_coordinador>', views.activar_coordinador, name='activar_coordinador'),
    path('coordinadores/desactivar/<int:id_coordinador>', views.desactivar_coordinador, name='desactivar_coordinador'),
    path('coordinadores/actualizar/<int:id_coordinador>', views.actualizar_coordinador, name='actualizar_coordinador'),
    # CLIENTES
    path('clientes/nuevo/', views.registrar_cliente, name='registrar_cliente'),
    path('clientes/listado/', views.listar_clientes, name='listar_clientes'),
    path('clientes/activar/<int:id_cliente>', views.activar_cliente, name='activar_cliente'),
    path('clientes/desactivar/<int:id_cliente>', views.desactivar_cliente, name='desactivar_cliente'),
    path('clientes/actualizar/<int:id_cliente>', views.actualizar_cliente, name='actualizar_cliente'),
    # SERVICIOS
    path('servicios/nuevo/', views.registrar_servicio, name='registrar_servicio'),
    path('servicios/listado/', views.listar_servicios, name='listar_servicios'),
    path('servicios/activar/<int:id_servicio>', views.activar_servicio, name='activar_servicio'),
    path('servicios/desactivar/<int:id_servicio>', views.desactivar_servicio, name='desactivar_servicio'),
    path('servicios/actualizar/<int:id_servicio>', views.actualizar_servicio, name='actualizar_servicio'),
    # RESERVAS
    path('reservas/nuevo', views.registrar_reservas, name = 'registrar_reserva'),
    path('reservas/listado/', views.listar_reservas, name='listar_reservas'),
    path('reservas/modificar/<int:id_reserva>', views.actualizar_reserva_de_servicio, name = 'actualizar_reserva'),    
    path('reservas/eliminar/<int:id_reserva>', views.eliminar_reserva, name='eliminar_reserva'),

]
