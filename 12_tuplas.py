#Las tuplas son estructuras de datos inmutables. Es decir, no puedes modificar una tupla a agregando o quitando un valor. Lo único que puedes hacer es definir de nuevo esa tupla a. Los objetos inmutables (como los strings) son tipos de datos para Python que apuntan a un lugar específico en memoria y que su contenido no puede ser cambiado. Al cambiar el contenido predefiniendo el contenido de la variable a, entonces cambiará su posición en memoria.

#Cómo trabajar con tuplas en Python
#Declarar tupla
mi_tupla = ()
mi_tupla = (1,2,3)
#Generar una tupla de 1 solo valor
#La , es obligatoria.

mi_tupla = (1,)
#Acceder a un índice de la tupla
mi_tupla = (1,2,3)
mi_tupla[0] #1
mi_tupla[1] #2
mi_tupla[2] #3
#Reasignar una tupla
mi_tupla = (1,2,3)
mi_otra_tupla = (4,5,6)
mi_tupla =+ mi_otra_tupla
#Métodos para trabajar con tuplas
#Usando el ejemplo:

mi_tupla = (1,1,1,2,2,3)
#Encontraremos los siguientes métodos:

mi_tupla.count(1)
# Devolverá 3, ya que el número 1 aparece 3 veces en la tupla.
mi_tupla.index(3)
#Devolverá 5, índice de la primera instancia donde se encuentra un elemento.
mi_tupla.index(1)
#Devolverá 0
mi_tupla.index(2)
#Devolverá 3.