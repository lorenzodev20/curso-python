def conversacion(mensaje):
    print('Hola, como estas? '+mensaje+". hasta luego...")

def run():
    mensaje = input(" - Por favor ingresa tu nombre: ")
    conversacion(mensaje)

if __name__ == '__main__':
    run()
