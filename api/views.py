from django.http import JsonResponse

from servicios.models import Coordinador, Empleado, Servicio


def listar_servicios_json(request):
    """
    Devuelve una lista de servicios en formato JSON.

    Parametro:
        request: La solicitud HTTP recibida por la vista.

    Retorna:
        JsonResponse: Un objeto JSON que contiene la lista de servicios.
    """
    servicios = Servicio.objects.all()
    servicios_data = []
    for servicio in servicios:
        servicio_data = {
            "id": servicio.id,
            "nombre": servicio.nombre,
            "precio": servicio.precio,
        }
        servicios_data.append(servicio_data)
    return JsonResponse(servicios_data, safe=False) #safe=False permite que se devuelva una lista en lugar de un diccionario.


def mostrar_servicio_json(request,id):
    """
    Retorna un objeto JSON que representa el servicio con el ID especificado.

    Parametros:
    - request: La solicitud HTTP recibida.
    - id: El ID del servicio a mostrar.

    Retorna:
    Un objeto JsonResponse con la información del servicio en formato JSON.

    Si no se encuentra el servicio con el ID especificado, se retorna una respuesta JSON vacía.

    """
    try:
        servicio = Servicio.objects.get(id=id)
        servicio_json = {
            "id": servicio.id,
            "nombre":servicio.nombre,
            "descripcion":servicio.descripcion,
            "precio": servicio.precio,
            }
        return JsonResponse(servicio_json)
    except Exception as error:
        return JsonResponse([],safe=False)


def listar_coordinadores_json(request):
    """
    Devuelve una lista de coordinadores en formato JSON.

    Parametro:
        request: La solicitud HTTP recibida por la vista.

    Retorna:
        JsonResponse: Un objeto JSON que contiene la lista de coordinadores.
    """
    coordinadores = Coordinador.objects.all()
    lista_coordinadores = list(coordinadores.values())
    return JsonResponse(lista_coordinadores, safe=False)


def listar_empleados_json(request):
    """
    Devuelve una lista de empleados en formato JSON.

    Parametro:
        request: La solicitud HTTP recibida por la vista.

    Retorna:
        JsonResponse: Un objeto JSON que contiene la lista de empleados.
    """
    empleados = Empleado.objects.all()
    lista_empleados = list(empleados.values())
    return JsonResponse(lista_empleados, safe=False)
