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
        primero = True
        for val in form.data:
            if primero:
                primero = False
                continue
            id = int(val)
            peliculas = Pelicula.objects.all()
            for p in peliculas:
                if p.id == id:
                    renta = Renta.objects.create(
                        id_usuario=request.user,
                        fecha=datetime.datetime.today()
                    )
                    DetalleRenta.objects.create(
                        id_renta=renta,
                        id_pelicula=p
                    )
                    p.stock -= 1
                    p.save()
        return redirect('renta')
    else:
        form = PeliculaForm()
    peliculas = Pelicula.objects.all()
    return render(request, 'panel_renta.html', {'peliculas': peliculas})

