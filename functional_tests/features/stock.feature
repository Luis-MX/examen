Característica: Panel de renta de pelicula
    Como usuario del sistema
    quiero poder iniciar sesion en el sistema
    para identificarme y registrar que peliculas rento.

    Escenario: Ver el panel de renta de peliculas
        Dado que ingreso los datos usuario "luis", contrasena "luis123"
        Cuando cuando me dirijo a la pagina "renta_peliculas"
        Entonces puedo ver el listado de peliculas y su stock
'''
    Escenario: Rentar varias peliculas disponibles
        Dado que ingreso los datos usuario "smithers", contrasena "boorns"
        Cuando presiono el botón de inicio de sesion: "Iniciar sesion"
        Entonces se motrara el mensaje "Datos incorrectos"

    Escenario: Rentar una pelicula con stock 0
        Dado que ingreso como un usuario anonimo
        Cuando accedo a "/usuarios/nuevo"
        Entonces recibo el mensaje de que la pagina no fue encontrada
'''
