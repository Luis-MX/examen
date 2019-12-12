from django.contrib import admin
from .models import Pelicula, Renta, DetalleRenta

admin.site.register(Pelicula)
admin.site.register(Renta)
admin.site.register(DetalleRenta)
