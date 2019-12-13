Característica: Panel de renta de pelicula
    Como usuario del sistema
    quiero poder iniciar sesion en el sistema
    para identificarme y registrar que peliculas rento.

    Escenario: Ver el panel de renta de peliculas
        Dado que ingreso los datos usuario "luis", contrasena "luis123"
        Cuando cuando me dirijo a la pagina "renta_peliculas"
        Entonces puedo ver el listado de peliculas y su stock

    Escenario: No selecciona niguna pelicula
        Dado que no he seleccionado peliculas
        Cuando presiono el boton rentar
        Entonces se muestra el mensaje "No se han seleccionado peliculas a rentar".

