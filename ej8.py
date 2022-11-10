#!/usr/bin/env python3
"""
Autor : Carlos López Herrero
Fecha   : 8/11/22
Propósito: lista de numeros consecutivos
"""


numero= int(input('dime un múmero positivo: '))

while numero<=0 :
     print('¡Te he pedido un número positivo!')
     numero=int(input('dime un número positivo: '))

for i in range (0,numero+1):
    print(i,end=', ')

print()
for i in range (numero,0-1,-1):
    print(i,end=', ')

print()
for i in range (1,numero):
    print(i,end=', ')

print()
for i in range (numero-1,0,-1):
    print(i,end=', ')

print()
for i in range (1,numero):
    print(i,ennd=', ')

