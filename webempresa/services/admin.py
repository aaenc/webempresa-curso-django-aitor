from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    # Para mostrar mas columnas en el listado (nombre del campo en el modelo)
    list_display = ('title', 'subtitle','image')

admin.site.register(Service,ServiceAdmin)
