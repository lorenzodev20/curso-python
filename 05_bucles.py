""" 05) Programas con Bucles While y For
"""
def runWhile():
    LIMITE = 1000000000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a "+str(contador)+" es igual a: "+str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


def runFor():
    LIMITE = 100

    for contador in range(LIMITE):
        print("Número: "+ str(contador))

if __name__ == '__main__':
    runWhile()
    runFor()