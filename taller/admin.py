from django.contrib import admin
from .models import Cliente, Reparacion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'direccion', 'edad')
    search_fields = ('nombre', 'correo', 'telefono')
    list_filter = ('nombre',)

class ReparacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'descripcion', 'fecha_ingreso', 'fecha_entrega', 'costo_formateado')
    search_fields = ('cliente__nombre', 'descripcion')
    list_filter = ('fecha_ingreso', 'fecha_entrega')

    @admin.display(description='Costo')
    def costo_formateado(self, obj):
        return f"${obj.costo:,}".replace(',', '.')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reparacion, ReparacionAdmin)