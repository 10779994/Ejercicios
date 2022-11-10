#calcular la tabla de multiplicar
numero= int(input('introduce un numero y calculare su tabla de multiplicar: '))
for i in range(0,11):
    print(f'{numero} x {i} = {numero*i}')
