from django.contrib import admin
from .models import Coordinador,Empleado,Servicio, Cliente, ReservaServicio
# Register your models here.

class CoordinadorAdmin(admin.ModelAdmin):
    model = Coordinador
    # muestra la info en columnas en el admin
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
    model = Cliente
    list_display = ['nombre', 'apellido', 'activo']
    search_fields = ['nombre', 'apellido']
    list_filter = ['activo']

class ReservaServicioAdmin(admin.ModelAdmin):
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
    

admin.site.register(Coordinador,CoordinadorAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Cliente)
admin.site.register(ReservaServicio, ReservaServicioAdmin)