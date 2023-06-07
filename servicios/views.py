from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse, get_object_or_404, redirect

from .models import Empleado,Coordinador,Cliente, ReservaServicio,Servicio



def index(request):
    lista_reservas = ReservaServicio.objects.all().order_by('-id')
    servicios = ReservaServicio.objects.count()
    clientes = Cliente.objects.count()
    empleados = Empleado.objects.count()
    reservas = ReservaServicio.objects.count()
    coordinadores = Coordinador.objects.count()
    context = {
        'lista_reservas':lista_reservas,
        'servicios':servicios,
        'clientes':clientes,
        'empleados':empleados,
        'reservas':reservas,
        'coordinadores':coordinadores,
        'title': 'Mi página de inicio',
        'message': '¡Hola, mundo!'
    }
    return render(request, 'index.html', context)


# FUNCIONES PARA EMPLEADO
def registrar_empleado(request):
    """
    View para procesar una solicitud POST para registrar un empleado en el sistema.
    
    Retorno:
    render: renderiza el template con los datos obtenidos
    """
    if request.POST:
        try:
            nombre_empleado = request.POST['nombre']
            apellido_empleado = request.POST['apellido']
            numero_legajo = request.POST['legajo']
            Empleado.objects.create(
                nombre = nombre_empleado,
                apellido = apellido_empleado,
                numero_legajo = numero_legajo
            )
            context={
                'creado':True
            }
            return render(
            request,
            "empleados/registrar.html",
            context
            )
        except:
            context={
                'fallo':True
            }
            return render(
            request,
            "empleados/registrar.html",
            context
            )
    return render(
        request,
        "empleados/registrar.html"
    )


def listar_empleados(request):
    """
    View para obtiener la lista de todos los empleados.

    Retorno:
    render: renderiza el template con la lista obtenida
    """
    empleados = Empleado.objects.all()
    context = {
        'empleados': empleados
    }
    return render(
        request,
        "empleados/listado.html",
        context
    )


def activar_empleado(request, id):
    """
    View para activar un registro de un empleado.

    Parametro:
    id (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de activar el registro
    redirect: Redirecciona al template del listado de empleados
    """
    try:
        empleado = Empleado.objects.get(id=id)
        if not (empleado.activo):
            empleado.activo = True
            empleado.save()            
            return redirect("listar_empleados")
    except ObjectDoesNotExist:
        return HttpResponse("El id no coincide con ningun objeto")
    

def desactivar_empleado(request, id):
    """
    View para desactivar un registro de un empleado.

    Parametro:
    id (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de desactivar el registro
    redirect: Redirecciona al template del listado de empleados
    """
    try:
        empleado = get_object_or_404(Empleado, id=id)
        empleado.activo = False
        empleado.save()
        return redirect("listar_empleados")
    except:
        return HttpResponse(f"No se ha podido activar el cliente {empleado.nombre} {empleado.apellido}")


def actualizar_empleado(request, id_empleado):
    """
    View para activar un registro de un empleado.

    Parametro:
    id_empleado (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de actualizar el registro
    render: renderiza el template del registro con los cambios
    """
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


# FUNCIONES PARA COORDINADOR
def registrar_coordinador(request):
    if request.method == 'POST':
        try:
            nombre_coordinador = request.POST["nombre"]
            apellido_coordinador = request.POST["apellido"]
            numero_documento_coordinador = request.POST["numero_documento"]
            fecha_alta_coordinador = request.POST["fecha_alta"]

            Coordinador.objects.create(
                nombre = nombre_coordinador,
                apellido = apellido_coordinador,
                numero_documento = numero_documento_coordinador,
                fecha_alta = fecha_alta_coordinador
            )
        except:
            return HttpResponse("Ocurrio un error al crear el coordinador")
    return render(
        request,
        "coordinadores/registrar.html"
    )


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


def activar_coordinador(request, id_coordinador):
    try:
        coordinador = Coordinador.objects.get(id=id_coordinador)
        if not (coordinador.activo):
            coordinador.activo = True
            coordinador.save()
            return HttpResponse("El registro del coordinador ingresado fué activado")
        else:
            return HttpResponse("Registro de coordinador ya activado")
    except ObjectDoesNotExist:
        return HttpResponse("El id no coincide con ningun objeto")


def desactivar_coordinador(request, id_coordinador):
    try:
        coordinador = Coordinador.objects.get(id=id_coordinador)
        if (coordinador.activo):
            coordinador.activo = False
            coordinador.save()
            return HttpResponse("El registro del coordinador ingresado fué desactivado")
        else:
            return HttpResponse("Registro de coordinador ya desactivado")
    except ObjectDoesNotExist:
        return HttpResponse("El id no coincide con ningun objeto")


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
            
            coordinador.nombre = nombre_coordinador
            coordinador.apellido = apellido_coordinador
            coordinador.numero_documento = numero_documento_coordinador
            coordinador.save()
    except:
        return HttpResponse("No se ha podido actualizar el registro del empleado") 
    
    return render(
        request,
        "coordinadores/actualizar.html",
        context
    )


# FUNCIONES PARA CLIENTE
def registrar_cliente(request):
    """
    View para procesar una solicitud POST para registrar un cliente en el sistema.
    
    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de guardar el registro
    render: renderiza el template con los datos obtenidos
    """
    if request.POST:
        try:
            nombre_cliente = request.POST['nombre']
            apellido_cliente = request.POST['apellido']
            Cliente.objects.create(
                nombre = nombre_cliente,
                apellido = apellido_cliente
            )
        except:
            return HttpResponse("Ocurrió un error al crear el usuario")
    return render(
        request,
        "clientes/registrar.html"
    )


def listar_clientes(request):
    """
    View para obtiener la lista de todos los clientes.

    Retorno:
    render: renderiza el template con la lista obtenida
    """
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(
        request,
        "clientes/listado.html",
        context
    )


def activar_cliente(request,id_cliente):
    """
    View para activar un registro de un cliente.

    Parametro:
    id_cliente (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de activar el registro
    redirect: Redirecciona al template del listado de clientes
    """
    try:
        cliente = Cliente.objects.get(id=id_cliente)
        cliente.activo = True
        cliente.save()
    except:
        return HttpResponse(f"No se ha podido activar el cliente {cliente.nombre} {cliente.apellido}")
    
    return redirect("listar_clientes")


def desactivar_cliente(request, id_cliente):
    """
    View para desactivar un registro de un cliente.

    Parametro:
    id_cliente (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de desactivar el registro
    redirect: Redirecciona al template del listado de clientes
    """
    try:
        cliente = Cliente.objects.get(id=id_cliente)
        cliente.activo = False
        cliente.save()
    except:
        return HttpResponse(f"No se ha podido desactivar el cliente {cliente.nombre} {cliente.apellido}")
    
    return redirect("listar_clientes")


def actualizar_cliente (request, id_cliente):
    """
    View para activar un registro de un cliente.

    Parametro:
    id_cliente (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de actualizar el registro
    render: renderiza el template del registro con los cambios
    """
    try:
        cliente = Cliente.objects.get(id=id_cliente)
        context = {
            "cliente": cliente
        }
        if request.POST:
            nombre_cliente = request.POST["nombre"]
            apellido_cliente = request.POST["apellido"]
            
            cliente.nombre = nombre_cliente
            cliente.apellido = apellido_cliente
            cliente.save()
    except:
        return HttpResponse("No se ha podido actualizar el registro del cliente") 
    
    return render(
        request,
        "clientes/actualizar.html",
        context
    )


# FUNCIONES PARA SERVICIO
def registrar_servicio(request):
    """
    View para procesar una solicitud POST para registrar un servicio en el sistema.
    
    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de guardar el registro
    render: renderiza el template con los datos obtenidos
    """
    if request.POST:
        try:
            nombre_servicio = request.POST['nombre']
            descripcion_servicio = request.POST['descripcion']
            precio_servicio= request.POST['precio']
            Servicio.objects.create(
                nombre = nombre_servicio,
                descripcion = descripcion_servicio,
                precio = precio_servicio,
                activo = True,
            )
        except:
            return HttpResponse("Ocurrio un problema al registrar el nuevo servicio")
    return render(request, 'servicios/registrar.html')


def listar_servicios(request):
    """
    View para obtiener la lista de todos los servicios.

    Retorno:
    render: renderiza el template con la lista obtenida
    """
    servicios = Servicio.objects.all()
    context = {
        'servicios': servicios
    }
    return render(
        request,
        "servicios/listado.html",
        context
    )


def activar_servicio(request, id_servicio):
    """
    View para activar un registro de un servicio.

    Parametro:
    id_servicio (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de activar el registro
    redirect: Redirecciona al template del listado de servicios
    """
    try:
        servicio = Servicio.objects.get(id=id_servicio)
        if not (servicio.activo):
            servicio.activo = True
            servicio.save()
            return redirect('listar_servicios')
        else:
            return HttpResponse("Registro de servicio ya activado")
    except ObjectDoesNotExist:
        return HttpResponse("El id no coincide con ningun objeto")


def desactivar_servicio(request,id_servicio):
    """
    View para desactivar un registro de un servicio.

    Parametro:
    id_servicio (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de desactivar el registro
    redirect: Redirecciona al template del listado de servicios.
    """
    try:
        servicio = Servicio.objects.get(id=id_servicio)
        if (servicio.activo):
            servicio.activo = False
            servicio.save()
            return redirect('listar_servicios')
        else:
            return HttpResponse("El registro del servicio ya está desactivado")
    except ObjectDoesNotExist:
        return HttpResponse("El id no coincide con ningun servicio")


def actualizar_servicio(request, id_servicio):
    """
    View para activar un registro de un servicio.

    Parametro:
    id_servicio (int): id del registro

    Retorno:
    HttpResponse: mensaje de que ocurrio un problema al tratar de actualizar el registro
    render: renderiza el template del registro con los cambios
    """
    try:
        servicio = Servicio.objects.get(id=id_servicio)
        context = {
            "servicio": servicio
        }
        if request.POST:
            nombre_servicio = request.POST["nombre"]
            descripcion_servicio = request.POST["descripcion"]
            precio_servicio = request.POST["precio"]
            
            servicio.nombre = nombre_servicio
            servicio.descripcion = descripcion_servicio
            servicio.precio = precio_servicio
            servicio.save()
    except:
        return HttpResponse("No se ha podido actualizar el registro del servicio") 
    
    return render(
        request,
        "servicios/actualizar.html",
        context
    )


# FUNCIONES PARA RESERVA
def registrar_reservas(request):
    if request.method == 'POST':
        try:
            fecha_reserva = request.POST['fecha_reserva']
            cliente_reserva = Cliente.objects.get(id = request.POST['clientes'])
            responsable_reserva = Coordinador.objects.get(id = request.POST['responsables'])
            empleado_reserva = Empleado.objects.get(id = request.POST['empleados'])
            servicio_reserva = Servicio.objects.get(id = request.POST['servicios'])
            precio_reserva = request.POST['precio']
            
            ReservaServicio.objects.create(
                fecha_reserva=fecha_reserva,
                cliente=cliente_reserva,
                responsable=responsable_reserva,
                empleado=empleado_reserva,
                servicio=servicio_reserva,
                precio=precio_reserva,
            )
            
            return HttpResponse("La reserva se ha registrado exitosamente")
        
        except Exception as e:
            return HttpResponse("Ocurrió un problema al registrar la nueva reserva: " + str(e))

    clientes = Cliente.objects.all()
    responsables = Coordinador.objects.all()
    empleados = Empleado.objects.all()
    servicios = Servicio.objects.all()

    context = {
        "clientes": clientes,
        "responsables": responsables,
        "empleados": empleados,
        "servicios": servicios,
    }

    return render(request, 'reservas/registrar.html', context)


def listar_reservas(request):
    reservas = ReservaServicio.objects.all()
    context = {
        'reservas':reservas
    }
    return render(
        request,
        "reservas/listado.html",
        context
    )


def actualizar_reserva_de_servicio(request, id_reserva):
    reserva = ReservaServicio.objects.get(id = id_reserva)
            
    if request.method == 'POST':
        try:
            reserva.fecha_reserva = request.POST['fecha_reserva']
            reserva.cliente = Cliente.objects.get(id = request.POST['clientes'])
            reserva.responsable= Coordinador.objects.get(id = request.POST['responsables'])
            reserva.empleado = Empleado.objects.get(id = request.POST['empleados'])
            reserva.servicio = Servicio.objects.get(id = request.POST['servicios'])
            reserva.precio = request.POST['precio']
            reserva.save()   
            
            return HttpResponse("La reserva se ha actualizado exitosamente")
        
        except Exception as e:
            return HttpResponse("Ocurrió un problema al actualizar la nueva reserva: " + str(e))

    clientes = Cliente.objects.all()
    responsables = Coordinador.objects.all()
    empleados = Empleado.objects.all()
    servicios = Servicio.objects.all()

    context = {
        "clientes": clientes,
        "responsables": responsables,
        "empleados": empleados,
        "servicios": servicios,
        "reserva": reserva,
        
    }

    return render(request, 'reservas/actualizar.html', context)


def eliminar_reserva(request, id_reserva):
    try:
        reserva = ReservaServicio.objects.get(id=id_reserva)
        reserva.delete()
    except:
        return HttpResponse("No se ha encontrado la reserva a eliminar.")

    return HttpResponse("Se ha eliminado la reserva correctamente.")




