#!/usr/bin/env python3
"""
Autor : Carlos López Herrero
Fecha   : 7/11/22
Propósito: escribir una lista de numeros consecutivos
"""
n= int(input("Escribe un numero: "))

if n>=0:
    for i in range(0,n+1):
       print(i,end=", ")
else:
    for i in range (0,n-1,-1):
        print(i,end=", ")

