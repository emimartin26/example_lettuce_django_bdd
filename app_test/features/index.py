#!/usr/bin/env python
#coding: utf8 

from django.contrib.auth.models import User
from lettuce import *
from nose.tools import assert_equals
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()


@step('Accedo a la url "(.*)"')
def accesso_url(step, url):
    world.response = world.browser.get(url)


@step('El servidor envia un codigo http ([0-9]+) de respuesta')
def comparar_server_respuesta(step, expected_code):
    code = world.response.status_code
    assert_equals(int(expected_code), code)

@step('Podemos ver "(.*)"')
def comparar_respuesta_contenido(step, expected_response):
    assert_equals(expected_response, world.response.content)

###############################################################################################################
@step(r'Soy un usuario autenticado')
def loggin_usuario(step, **kwargs):
    user = User.objects.create_user('emi', '1@1.com', 'testpass')
    world.browser.login(username='emi', password='testpass')

