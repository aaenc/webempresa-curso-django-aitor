from .models import Link
from django.core.exceptions import FieldDoesNotExist

# Disccinario de contexto
# hay que añadir en settings.py de webempresa en :
#   TEMPLATES -> OPTIONS -> context_processors como "social.processors.ctx_dict" 
def redes_sociales(request):
    redes = []
    for link in Link.objects.all():
        try:
            clase = link.clase
        except FieldDoesNotExist:
            clase = None
        redes.append({
            'key': link.key,
            'url': link.url,
            'nombre': link.name,
            'clase': link.clase,  # Ahora es seguro
            'activo': link.activo,
        })
    return {'redes': redes}  # Lo que sera accesible desde todas las paginas sera "redes"