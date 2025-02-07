from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    descripcion = models.TextField(null=True, verbose_name='Descripción')

    def __str__(self):
        fila = "Título: " + self.titulo + "-" + " Descripción: " + self.descripcion
        return fila
    
    #Aqui lo que se hace es que cuando se elimine un libro, se elimine también la imagen asociada a este
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()