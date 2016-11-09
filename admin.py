from django.contrib import admin
from .models import Estado, Municipio, Ubicacion
# Register your models here.

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('iidestado', 'cdescripcion',)
    search_fields = ('cdescripcion',)


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('iidmunicipio', 'cdescripcion',)
    search_fields = ('cdescripcion',)


class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('iidubicacion', 'iasentamiento', 'cdescripcion',
                    'icodigopostal',)
    search_fields = ('cdescripcion',)
    list_filter = ('icodigopostal',)

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)