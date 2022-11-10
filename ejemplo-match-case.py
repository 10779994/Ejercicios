#Ejemplo uso de match-case

#Pedimos el primer numero
numero1= int(input('introduce el primer numero: '))
#Pedimos el segundo numero
numero2= int(input('introduce el segundo numero: '))

#Pedimos la operacion a realizar
operacion= input('Introduce la operacion a ralizar (+,-,*,/): ')

match operacion:
    case '+': 
        resultado= numero1 + numero2
    case '-':
        resultado= numero1 - numero2
    case '*':
        resultado= numero1 * numero2
    case '/':
        resultado = numero1 / numero2
    case _:
        print('Opcion no valida')
    
print(f'El resultado es: {resultado}')


