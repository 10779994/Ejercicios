#!/usr/bin/env python3
"""
Autor : Carlos López Herrero
Fecha   : 10/11/22
Propósito: Calculo de la anchura y altura de un rectangulo
"""

anchura=int(input('Anchura del rectángulo: '))
altura=int(input('Altura del rectángulo: '))

for i in range(altura):
    for j in range(anchura):
        print('*', end=' ')
    print()

