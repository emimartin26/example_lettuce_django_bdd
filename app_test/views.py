#!/usr/bin/env python
#coding: utf8 
from django.shortcuts import render
from django.http import HttpResponse
 
def view_test(request):
	if(request.user.is_authenticated()):
		respuesta = "Bienvenido Usuario autenticado"
	else:
		respuesta = "Bienvenido Usuario Anonimo"

	return HttpResponse(respuesta);