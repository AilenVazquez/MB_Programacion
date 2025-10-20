# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

import math

numeros_input = input("Ingrese una lista de numeros separados por espacio: ")
numeros_cadena = numeros_input.split()
numeros_lista = list(map(int, numeros_cadena))
cuadrados = []

def calcular_cuadrados(numeros_lista):
    for n in numeros_lista:
        cuadrado = n ** 2
        cuadrados.append(cuadrado)
    return cuadrados

print("Los cuadrados de los numeros son", calcular_cuadrados(numeros_lista))

# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

def calcular_estadisticas(numeros_lista):
    media = sum(numeros_lista) / len(numeros_lista)
    
    diferencia = 0
    for x in numeros_lista:
        dif = (x - media) ** 2
        diferencia += dif
    varianza = diferencia / len(numeros_lista)
    
    desviacion_tipica = round(math.sqrt(varianza),2)
    return {
        "media": media,
        "varianza": varianza,
        "desviacion_tipica": desviacion_tipica
    } 
    
print("Las estadisticas de los numeros son", calcular_estadisticas(numeros_lista))