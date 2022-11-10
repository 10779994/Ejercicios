#!/usr/bin/env python3
"""
Autor : Carlos López <10779994@iespenyagolosa.es>
Fecha   : 26/10/22
Propósito: Calculo de ecuaciones de segundo grado
"""

print('calculos de ecuaciones de segundo grado')
variable_a = float(input('Escribe el valor de a: '))
variable_b = float(input('Escribe el valor de b: '))
variable_c = float(input('Escribe el valor de c: '))
solucion_1= int(-variable_b+(variable_b**2-4*variable_a*variable_c)**(1/2))/(2*variable_a)
solucion_2= int(-variable_b-(variable_b**2-4*variable_a*variable_c)**(1/2))/(2*variable_a)
print(f'las soluciones de la ecuación son {solucion_1} y {solucion_2} ')