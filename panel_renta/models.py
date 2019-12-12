from django.db import models
from django.contrib.auth.models import User

class Pelicula(models.Model):
    titulo = models.TextField(verbose_name='titulo', name='titulo', unique=True, db_column='titulo', max_length=50)
    genero = models.TextField(verbose_name='genero', name='genero', db_column='genero', max_length=50)
    duracion = models.IntegerField(verbose_name='duracion', name='duracion', db_column='duracion')
    descripcion = models.TextField(verbose_name='descripcion', name='descripcion', db_column='descripcion', max_length=500)
    stock = models.IntegerField(verbose_name='stock', name='stock', db_column='stock')

    def __str__(self):
        return self.titulo + ' - ' + str(self.duracion) + ' duracion'

class Renta(models.Model):
    id_usuario = models.ForeignKey(User, verbose_name="IdUsuario", on_delete=models.CASCADE)
    fecha = models.DateField("fecha")

    def __str__(self):
        return str(self.id_usuario) + str(self.fecha)
    

class DetalleRenta(models.Model):

    id_renta = models.ForeignKey(Renta, verbose_name="IdRenta", on_delete=models.CASCADE)
    id_pelicula = models.ForeignKey(Pelicula, verbose_name="IdPelicula", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DetalleRenta"
        verbose_name_plural = "DetalleRentas"

    def __str__(self):
        return 'Renta de: ' + str(self.id_renta)


