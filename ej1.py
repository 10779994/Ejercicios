#!/usr/bin/env python3
"""
Autor : Carlos López <10779994@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Conversión de grados celsius a fahrenheit
"""

print('convertidor de grados Celsius a fahrenheit')
gradosC = float(input('Escribe una temperatura en grados Celsius: '))
gradosF = 1.8*gradosC + 32
print(f'{gradosC} ºC son {gradosF} ºF')