from django.test import TestCase
from panel_renta.models import Pelicula
from django.core.exceptions import ValidationError
from unittest import skip
from django.contrib.auth.models import User

class TestViews(TestCase):


    def test_acceso_a_pagina(self):
        User.objects.create_user(username='luis', password='luis123')
        self.client.login(username='luis', password='luis123')
        response = self.client.get('/renta_peliculas')

        self.assertEquals(response.status_code, 200)

    def test_url_renta  (self):
        self.test_acceso_a_pagina()
        response = self.client.get('/renta_peliculas')
        self.assertEqual(response.status_code, 200)

    def test_template_correcto(self):
        self.test_acceso_a_pagina()
        response = self.client.get('/renta_peliculas')
        self.assertTemplateUsed(response, 'panel_renta.html')


    def test_POST_redirects_to_itself(self):
        self.test_acceso_a_pagina()

        response = self.client.post(
            '/renta_peliculas',
            data={'1': '1', '2': '2'}
        )
        self.assertRedirects(response, '/renta_peliculas')



    def test_for_invalid_input_shows_error_on_page(self):
        self.test_acceso_a_pagina()
        response = self.client.post(
            '/renta_peliculas',
            data={}
        )
        self.assertContains(response, 'No se han seleccionado peliculas a rentar')
