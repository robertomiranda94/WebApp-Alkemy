from django.urls import path
from . import views

urlpatterns = [
    path('api/servicios', views.listar_servicios_json, name = "listar_servicios_json")
]