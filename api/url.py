from django.urls import path
from . import views

urlpatterns = [
    path('api/servicios', views.listar_servicios_json, name = "listar_servicios_json"),
    path('api/servicios/<int:id>', views.mostrar_servicio_json, name = "mostrar_servicio_json")

]