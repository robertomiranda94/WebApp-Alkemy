from django.shortcuts import render,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Empleado

# Create your views here.

def index(request):
    context = {
        'title': 'Mi página de inicio',
        'message': '¡Hola, mundo!'
    }
    return render(request, 'index.html', context)

def registrar_empleado(request):
    if request.POST:
        try:
            nombre_empleado = request.POST['nombre']
            apellido_empleado = request.POST['apellido']
            numero_legajo = request.POST['legajo']
            Empleado.objects.create(
                nombre = nombre_empleado,
                apellido = apellido_empleado,
                numero_legajo = numero_legajo,
                activo = True
            )
        except:
            return HttpResponse("Ocurrió un error al crear el usuario")
    return render(
        request,
        "empleados/registrar.html"
    )

def activar_registro_empleado(request, id):
    try:
        empleado = Empleado.objects.get(id=id)
        if not (empleado.activo):
            empleado.activo = True
            empleado.save()
            return HttpResponse("El registro del empleado ingresado ha sido activado")
        else:
            return HttpResponse("No es necesario activar el registro de empleado")             
    except ObjectDoesNotExist:
        return HttpResponse("El id no coincide con ningun objeto")
    
    

    
    
    
