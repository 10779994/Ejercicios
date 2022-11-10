#!/usr/bin/env python3
"""
Autor : Carlos López Herrero
Fecha   : 3/11/22
Propósito: adivinar el numero del programa
"""

from random import randrange

num1=int(input('Valor mínimo: '))
num2=int(input('Valor máximo: '))
aleatorio= randrange(num1,num2)
intentos =0
print(f'a ver si adivinas un número entero entre {num1} y {num2}')

numero=int(input('Escribe un número: '))

while numero != aleatorio: 
    intentos +=1
    if numero < aleatorio:
        numero= int(input('Demasiado pequeño, intentalo de nuevo: '))
    else:
        numero= int(input('Demasiado grande, intentalo de nyevo: '))

print(f'Acertaste, te ha costado {intentos} intentos ')