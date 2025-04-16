from django.db import models
class Articulos(models.Model): #Define la estructura de nuestra tabla
    articulo = models.TextField() #Texto largo
    marca = models.TextField()
    modelo = models.TextField()
    serie = models.TextField()
    caracteristicas  = models.TextField()
    estado = models.CharField(max_length=10)
    n_inventario = models.TextField()
    resguardante = models.CharField(max_length=255)
    area = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name = "Articulos"
        ordering = ["-created"]
        #el menos indica que se ordenara del mas reciente al mas viejo 
    def __str__(self):
      return self.articulo
#Indica que se mostrára el nombre como valor en la tabla

# Create your models here.
