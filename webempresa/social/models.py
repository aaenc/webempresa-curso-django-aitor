from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=100,verbose_name="NombreClave",unique=True) ## Para no permitir caracteres especiales
    name = models.CharField(max_length=200,verbose_name="Red Social")
    url = models.URLField(max_length=200,verbose_name="Enlace", null=True,blank=True)
    clase = models.CharField(max_length=200,verbose_name="Clase", null=True,blank=True,default="")
    activo = models.BooleanField(default=True, verbose_name="¿Activo?")  # ✅ Nuevo campo booleano
    # Estos dos como son automaticos al final
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name='enlace'
        verbose_name_plural='enlaces'
        ordering = ["-name"]
        
    def __str__(self):
        return self.name     
