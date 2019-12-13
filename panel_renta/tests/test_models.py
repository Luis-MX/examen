from django.test import TestCase
from panel_renta.models import Pelicula
from django.core.exceptions import ValidationError
from unittest import skip


class TestModels(TestCase):

    def setUp(self):
        self.pelicula = Pelicula(
            titulo='Juegos',
            genero='fiction',
            duracion=3,
            descripcion='aaaaaaa',
            stock=5
        )

    def test_agrega_pelicula(self):
        self.pelicula.save()
        self.assertEqual(Pelicula.objects.count(), 1)

    def test_max_length(self):
        self.pelicula.titulo = 'a'*51
        with self.assertRaises(ValidationError):
            self.pelicula.full_clean()

    def test_min_length(self):
        self.pelicula.stock -= 6
        with self.assertRaises(ValidationError):
            self.pelicula.full_clean()

    def test_titulo_solo_letras(self):
        self.pelicula.titulo= ''
        with self.assertRaises(ValidationError):
            self.pelicula.full_clean()


