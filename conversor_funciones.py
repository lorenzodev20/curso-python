#convierte pesos mexicanos, argentinos y colombianos a dólares usando funciones

# Funcion Conversor
def conversor(tipo_pesos, tipo_de_cambio):
    dolares = 0
    #pregunto al usuario la cantidad a convertir y convierto a float para mejor manejo de datos
    pesos = float(input('¿Cuántos pesos '+tipo_pesos+' tienes?: '))
    #hago la conversión
    dolares = pesos / tipo_de_cambio
    #redondeo los dólares a dos decimales
    dolares = round(dolares, 2)
    #convierto el float de dolares a un string
    dolares = str(dolares)
    #imprimo el valor de la conversion. Se pueden sumar (concatenar) strings con '+'
    print('Tienes $' + dolares +' dólares')

# """ """ permite crear strings multilineas
menu = """
Bienvenido al conversor de monedas

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opción:

"""
# de derecha a izquierda: llamo a la funcion input, le paso la variable menu para que la imprima y reciba el número que el usuario escogió, lo convierto a int y lo guardo en la variable 'opcion'
opcion = int(input(menu))

if opcion == 1: #pesos mexicanos
    tipo_de_cambio = 21.5
    conversor("mexicanos", tipo_de_cambio)
elif opcion == 2: #pesos colombianos
    tipo_de_cambio = 4436.88
    conversor("colombianos", tipo_de_cambio)
elif opcion == 3: #pesos argentinos
    tipo_de_cambio = 74.44
    conversor("argentinos", tipo_de_cambio)
else:  #el usuario escribió algo diferente
	print('Escribe una opción correcta: ')
