from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from .forms import PeliculaForm
from .models import Pelicula, Renta, DetalleRenta

@login_required
def panel_renta(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if len(form.data) < 2:
            peliculas = Pelicula.objects.all()
            return render(request, 'panel_renta.html', {'peliculas': peliculas, 'error': True, 'error_message': 'No se han seleccionado peliculas a rentar'})
        for campo in form.data:
            if not campo.isnumeric():
                continue
            peliculas = Pelicula.objects.all()
            peliculas = list(filter(lambda item: item.id == int(campo), peliculas))
            for p in peliculas:
                renta = Renta.objects.create(id_usuario=request.user, fecha=datetime.datetime.today())
                DetalleRenta.objects.create(id_renta=renta, id_pelicula=p)
                p.stock -= 1
                p.save()
        return redirect('renta')
    else:
        form = PeliculaForm()
    peliculas = Pelicula.objects.all()
    return render(request, 'panel_renta.html', {'peliculas': peliculas, 'error': False, 'error_message': ''})

