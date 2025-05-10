from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    #content = models.TextField(verbose_name="Contenido")
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden",default=0)
    # Estos dos como son automaticos al final
    activo = models.BooleanField(default=True, verbose_name="¿Activo?")  # ✅ Nuevo campo booleano
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name='pagina'
        verbose_name_plural='paginas'
        ordering = ["order","-title"]
        
    def __str__(self):
        return self.title     
