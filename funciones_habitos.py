#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:56:52 2026

@author: victoriamochnacs
"""
#funcion 1
def registrar_habitos ():
    lista_actividades = []
    pregunta_habitos = input ("¿Desea agregar datos?")
    while (pregunta_habitos == "Si") or (pregunta_habitos == "si") or (pregunta_habitos == "Sí") or (pregunta_habitos == "sí"):
        datos_habitos = input("Ingresar actividad")
        lista_actividades.append(datos_habitos)
        pregunta_habitos = input("¿Desea ingresar más datos?")
        if pregunta_habitos == "No" or pregunta_habitos == "no":
            break
    return lista_actividades


resumen = registrar_habitos ()
print(resumen)

#funcion 2
def analizar_habitos (lista_actividades):
    diccio= {}
    for i in lista_actividades:
        if i not in diccio:
            diccio[i]=1
        else:
            diccio[i]+=1
    return diccio