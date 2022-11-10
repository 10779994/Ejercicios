#!/usr/bin/env python3
"""
Autor : Carlos López Herrero
Fecha   : 10/11/22
Propósito: Cambiar vocales de una frase
"""

frase = 'Tengo una hormiga en la barriga '
vocal=input('Dime una vocal: ')
VOCALES='aeiou'
frase_nueva= []

for i in range (len(frase)):
    if frase[i] in VOCALES:
        frase_nueva.append(vocal)
    else:
        frase_nueva.append(frase[i])

print(f'la frase es ahora: {frase_nueva}' )

