from django.shortcuts import render,HttpResponse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Empleado,Coordinador

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

def listar_empleados(request):
    empleados = Empleado.objects.all()
    context = {
        'empleados': empleados
    }
    return render(
        request,
        "empleados/listado.html",
        context
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

def actualizar_empleado(request, id_empleado):
    try:
        empleado = Empleado.objects.get(id=id_empleado)

        context = {
            "empleado": empleado
        }

        if request.POST:
            nombre_empleado = request.POST["nombre"]
            apellido_empleado = request.POST["apellido"]
            legajo_empleado = request.POST["numero_legajo"]


            empleado.nombre = nombre_empleado
            empleado.apellido = apellido_empleado
            empleado.numero_legajo = legajo_empleado

            empleado.save()
    except:
        return HttpResponse("No se ha podido actualizar el registro del empleado") 
    
    return render(
        request,
        "empleados/actualizar.html",
        context
    )

def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.activo = False
    empleado.save()
    return HttpResponse("El registro del empleado ingresado fué sido desactivado")

def listar_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    context = {
        'coordinadores': coordinadores
    }
    return render(
        request,
        "coordinadores/listado.html",
        context
    )

def actualizar_coordinador(request,id_coordinador):
    try:
        coordinador = Coordinador.objects.get(id=id_coordinador)
        context = {
            "coordinador": coordinador
        }
        if request.POST:
            nombre_coordinador = request.POST["nombre"]
            apellido_coordinador = request.POST["apellido"]
            numero_documento_coordinador = request.POST["numero_documento"]
            fecha_alta_coordinador = request.POST["fecha_alta"]
            activo_coordinador = request.POST["activo"]
            
            coordinador.nombre = nombre_coordinador
            coordinador.apellido = apellido_coordinador
            coordinador.numero_documento = numero_documento_coordinador
            coordinador.activo = activo_coordinador
            coordinador.save()
    except:
        return HttpResponse("No se ha podido actualizar el registro del empleado") 
    
    return render(
        request,
        "coordinadores/actualizar.html",
        context
    )

def desactivar_cliente(request, id_cliente):
    try:
        cliente = Cliente.objects.get(id=id_cliente)
        cliente.activo = False
        cliente.save()
    except:
        return HttpResponse(f"No se ha podido desactivar el cliente {cliente.nombre} {cliente.apellido}")
    
    return redirect("listar_clientes")
