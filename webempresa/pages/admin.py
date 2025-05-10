from django.contrib import admin
from .models import Page

# Register your models here.

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    # Para mostrar mas columnas en el listado (nombre del campo en el modelo)
    list_display = ('title', 'activo','order')

admin.site.register(Page,PageAdmin)
