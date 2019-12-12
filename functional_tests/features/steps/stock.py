from behave import given, when, then
from selenium import webdriver
from unittest import TestCase
import time

@given(u'que ingreso los datos usuario "{usuario}", contrasena "{password}"')
def step_impl(context, usuario, password):
    time.sleep(2)
    context.driver.get(context.url + '/admin/login')
    time.sleep(0.5)
    entrada_usuario = context.driver.find_element_by_id('id_username')
    entrada_usuario.send_keys(usuario)
    entrada_password = context.driver.find_element_by_id('id_password')
    entrada_password.send_keys(password)
    boton_envio = context.driver.find_elements_by_tag_name('input')[-1]
    boton_envio.click()
    time.sleep(2)


@when(u'cuando me dirijo a la pagina "{renta_peliculas}"')
def step_impl(context, renta_peliculas):
    context.driver.get(context.url + f'/{renta_peliculas}')


@then(u'puedo ver el listado de peliculas y su stock')
def step_impl(context):
    time.sleep(3)