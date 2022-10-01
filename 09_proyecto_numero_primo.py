"""
Proyecto: Número Primo.
Con el numero ingresado se valida si el numero es primo o no.
"""

def numero_primo():
    numero = int(input('Ingrese el numero: '))
    for i in range(2,numero):
        if (numero%i) == 0:
            return False
    return True

if __name__ == '__main__':
    result = numero_primo()
    if (result):
        print('El número es primo')
    else:
        print('El número NO es primo')