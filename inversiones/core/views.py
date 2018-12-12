# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from core.models import Cliente

class ListaClientes(ListView):
	model = Cliente
