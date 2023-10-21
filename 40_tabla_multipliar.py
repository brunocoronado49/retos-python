'''
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
'''


def tabla_multiplicar(numero):
    result = 0
    try:
        for num in range(1, 11):
            print(f'{numero} x {num} = {numero * num}')
    except ValueError:
        print('Ingresa un numero válido')
        

numero = int(input('Ingresa un numero: '))
tabla_multiplicar(numero)