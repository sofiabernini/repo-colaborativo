# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:04:50 2026

@author: sofia
"""

import funciones_habitos
lista = funciones_habitos.registrar_habitos()
resultado = funciones_habitos.analizar_habitos(lista)
print("Resumen de actividades:")
print(resultado)