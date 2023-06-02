from django.shortcuts import render
from django.http import JsonResponse

from servicios.models import Servicio 


# Create your views here.
def listar_servicios_json(request):
    servicios = Servicio.objects.all()

    servicios_data = []
    for servicio in servicios:
        servicio_data = {
            "id": servicio.id,
            "nombre": servicio.nombre,
            "precio": servicio.precio,
        }
        servicios_data.append(servicio_data)
    return JsonResponse(servicios_data, safe = False) #safe=False permite que se devuelva una lista en lugar de un diccionario.



