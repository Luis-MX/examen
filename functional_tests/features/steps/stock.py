from behave import given, when, then
from selenium import webdriver
from unittest import TestCase
import time

@given(u'que ingreso los datos usuario "{usuario}", contrasena "{password}"')
def step_impl(context, usuario, password):
    context.driver.get(context.url + '/admin/login')
    time.sleep(1)
    entrada_usuario = context.driver.find_element_by_id('id_username')
    entrada_usuario.send_keys(usuario)
    entrada_password = context.driver.find_element_by_id('id_password')
    entrada_password.send_keys(password)
    boton_envio = context.driver.find_elements_by_tag_name('input')[-1]
    boton_envio.click()
    time.sleep(0.5)


@when(u'cuando me dirijo a la pagina "{renta_peliculas}"')
def step_impl(context, renta_peliculas):
    context.driver.get(context.url + f'/{renta_peliculas}')


@then(u'puedo ver el listado de peliculas y su stock')
def step_impl(context):
    context.test.assertIn('peliculas', context.driver.title)
    time.sleep(1)


@given(u'que no he seleccionado peliculas')
def step_impl(context):
    context.driver.get(context.url + '/renta_peliculas')


@when(u'presiono el boton rentar')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id('rentar').click()
    time.sleep(1)

@then(u'se muestra el mensaje "{mensaje}".')
def step_impl(context, mensaje):
    text = context.driver.find_element_by_id('mensaje_error').text
    context.test.assertEquals(text, mensaje)

