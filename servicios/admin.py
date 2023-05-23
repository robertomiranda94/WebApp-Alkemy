from django.contrib import admin
from .models import Coordinador
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
    
    
admin.site.register(Coordinador,CoordinadorAdmin)