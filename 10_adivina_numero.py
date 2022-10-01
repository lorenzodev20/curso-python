"""
Proyecto: Adivina el Número
"""
from ast import While
import random

def run():
    inicio = 1
    fin = 100
    numero_aleatorio = random.randint(inicio,fin)
    numero_elegido = int(input('Elige un numero entre '+str(inicio)+' y '+str(fin)+': '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido<numero_aleatorio:
            print('Busca un número mas grande.')
        else:
            print('Busca un número mas pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('Ganaste!!!.')

if __name__ == '__main__':
    run()