#!/usr/bin/env python3
"""
Autor : Carlos López <10779994@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de segundos a minutos
"""

print('convertidor de segundos a minutos')
Segundos = float(input('Escribe un tiempo en segundos: '))
Minutos= Segundos//60
print(f'{Segundos} s son {Minutos} min')