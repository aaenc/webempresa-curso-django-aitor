from django.contrib import admin
from .models import Link

# Register your models here.

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return  ('key','name','clase')
        else:
            return  ('created','updated')

    # Para mostrar mas columnas en el listado (nombre del campo en el modelo)
    list_display = ('key', 'name','clase','activo','url')

admin.site.register(Link,LinkAdmin)
