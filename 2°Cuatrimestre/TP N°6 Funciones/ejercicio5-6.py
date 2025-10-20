# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

import math

radio = int(input("Ingrese el radio del circulo: "))
altura = int(input("Ingrese la altura del cilindro: "))

def area_circulo(radio):
    area = math.pi * radio ** 2
    return round(area, 2)

def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)
    volumen = area_base * altura
    return round(volumen, 2)

print("El area del circulo es", area_circulo(radio),"y el volumen del cilindro es", volumen_cilindro(radio, altura))


# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

numeros_input = input("Ingrese una lista de numeros separados por espacio: ")
numeros_cadena = numeros_input.split()
numeros_lista = list(map(int, numeros_cadena))

def calcular_media(numeros_lista):
    media = 0
    for n in numeros_lista:
        media += n
    media = media / len(numeros_lista)
    return media


print("La media de los numeros es", calcular_media(numeros_lista))