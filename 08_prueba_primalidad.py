"""
Proyecto 1: Prueba de Primalidad

En este ejemplo, aprenderemos cómo detectar si un número es primo en Python.
Esto se conoce como prueba de primalidad. Un número primo es todo número que puede dividirse únicamente por sí mismo y por 1. Todos los números primos, excepto el 2, son impares.
En la matemática aplicada, los números primos son utilizados para generar códigos criptográficos seguros.
Esto se logra empleando los números primos de Mersenne (números muy grandes).

"""
def es_primo(numero):
    contador = 0
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % 1 == 0:
            contador +=1
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo.')
    else:
        print('No es primo.')

if __name__ == '__main__':
    run()