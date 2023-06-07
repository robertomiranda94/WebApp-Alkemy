from django.http import JsonResponse

from servicios.models import Servicio, Cliente, Empleado, Coordinador


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


def mostrar_servicio_json(request,id):
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
    

def listar_clientes_json(request):
    clientes = Cliente.objects.all()
    clientes_data = []
    for cliente in clientes:
        cliente_data = {
            "id": cliente.id,
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
        }
        clientes_data.append(cliente_data)
    return JsonResponse(clientes_data, safe = False) #safe=False permite que se devuelva una lista en lugar de un diccionario.


def listar_empleados_json(request):
    empleados = Empleado.objects.all()
    empleados_data = []
    for empleado in empleados:
        empleado_data = {
            "id": empleado.id,
            "nombre": empleado.nombre,
            "apellido": empleado.apellido,
            "numero_legajo":empleado.numero_legajo
        }
        empleados_data.append(empleado_data)
    return JsonResponse(empleados_data, safe = False) #safe=False permite que se devuelva una lista en lugar de un diccionario.


def listar_coordinadores_json(request):
    coordinadores = Coordinador.objects.all()
    coordinadores_data = []
    for coordinador in coordinadores:
        coordinador_data = {
            "id": coordinador.id,
            "nombre": coordinador.nombre,
            "apellido": coordinador.apellido,
            "numero_documento":coordinador.numero_documento,
            "fecha_alta":coordinador.fecha_alta
        }
        coordinadores_data.append(coordinador_data)
    return JsonResponse(coordinadores_data, safe = False) #safe=False permite que se devuelva una lista en lugar de un diccionario.
