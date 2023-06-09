from django.contrib import admin
from .models import Coordinador,Empleado,Servicio, Cliente, ReservaServicio
# Register your models here.

class CoordinadorAdmin(admin.ModelAdmin):
    model = Coordinador
    """
    Clase de administración personalizada para el modelo Coordinador.
    """
    list_display = [
        "id",
        "nombre",
        "apellido",
        "numero_documento",
        "fecha_alta",
        "activo"
    ]

    # busqueda por fields
    search_fields = [
        "nombre",
        "apellido",
    ]
    list_filter = [
        "activo"
    ]

class EmpleadoAdmin(admin.ModelAdmin):
    """
    Clase de administración personalizada para el modelo Empleado.
    """
    model = Empleado
    list_display = [
        "nombre",
        "apellido",
        "numero_legajo",
        "activo"
    ]

    search_fields = [
        "nombre",
        "apellido",
    ]
    
    list_filter = [
        "activo"
    ]
    
    

class ServicioAdmin(admin.ModelAdmin):
    """
    Clase de administración personalizada para el modelo Servicio.
    """
    model = Servicio
    list_display = [
        "id",
        "nombre",
        "descripcion",
        "precio",
        "activo"
    ]


    search_fields = [
        "nombre"
    ]


    list_filter = [
        "activo"
    ]

class ClienteAdmin(admin.ModelAdmin):
    """
    Clase de administración personalizada para el modelo Cliente.
    """
    model = Cliente
    list_display = ['nombre', 'apellido', 'activo']
    search_fields = ['nombre', 'apellido']
    list_filter = ['activo']

class ReservaServicioAdmin(admin.ModelAdmin):
    """
    Clase de administración personalizada para el modelo ReservaServicio.
    """
    model = ReservaServicio
    list_display = [
        "id",
        "fecha_creacion",
        "fecha_reserva",
        "cliente",
        "responsable",
        "empleado",
        "servicio",
        "precio",

    ]


    search_fields = [
        "responsable__nombre",
        "cliente__nombre",
        "empleado__nombre",
        "servicio__nombre",
    ]

""""
Se registra cada clase de modelo junto con su clase de administrador correspondiente en el panel de administración de Django mediante el uso de admin.site.register()
"""

admin.site.register(Coordinador,CoordinadorAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Cliente)
admin.site.register(ReservaServicio, ReservaServicioAdmin)