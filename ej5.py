#!/usr/bin/env python3
"""
Autor : Carlos López <10779994@iespenyagolosa.es>
Fecha   : 31/10/22
Propósito: Calculo de areas
"""

print('cálculo de áreas - Elige una figura geométrica: ')
print('a) Triángulo')
print('b) Círculo')
figura=input('¿que figura quieres calcular (escribe T o C)?').upper()
if figura=='T':
     base=float(input('escribe la base: '))
     altura=float(input('escribe la altura: '))
     area=base*altura/2
     print(f'Un triangulo de base {base} y altura {altura} tiene un área de {area}')
elif figura=='C':
     radio=float(input('escribe el radio: '))
     area=3.14*radio**2
     print(f'Un circulo de radio {radio} tiene un area de {area}')
