#!/usr/bin/env python3
"""
Autor : Carlos López <10779994@iespenyagolosa.es>
Fecha   : 26/10/22
Propósito: Calculo de años
"""

año_actual = int(input('¿En que año estamos?: '))
año_cualquiera= int(input('Escribe un año cualquiera: '))
otro_año= año_actual-año_cualquiera
print(f'Para llegar al año {año_actual} faltan {otro_año} años')