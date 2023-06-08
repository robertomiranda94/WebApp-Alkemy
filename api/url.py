from django.urls import path
from . import views

urlpatterns = [
    path('api/servicios', views.listar_servicios_json, name="listar_servicios_json"),
    path('api/coordinadores', views.listar_coordinadores_json, name="listar_coordinadores"),
    path('api/servicios/<int:id>', views.mostrar_servicio_json, name="mostrar_servicio_json"),
    path('api/empleados', views.listar_empleados_json, name='listar_empleados'),

]