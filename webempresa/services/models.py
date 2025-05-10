from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    subtitle = models.CharField(max_length=200,verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen",upload_to="services")
    # Estos dos como son automaticos al final
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering = ["-created"]
        
    def __str__(self):
        return self.title     

