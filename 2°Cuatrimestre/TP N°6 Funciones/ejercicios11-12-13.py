# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

cadena = input("Ingrese una cadena de caracteres: ")
frecuencia_palabras = {}

lista = cadena.split()

for palabra in lista:
    frecuencia_palabras[palabra] = lista.count(palabra)
            
print(frecuencia_palabras)



# Ejercicio 12:  para tener en cuenta
# https://vm.tiktok.com/ZMASa9Avw/

from googletrans import Translator

traductor = Translator()
print(traductor.translate('Hola, ¿cómo estás?', dest='en').text)




# Ejercicio 13: funciones
# https://www.tiktok.com/@programaconmica/video/7527416777941306629?_r=1&_t=ZM-8zCriuJVWzw

lista = [1,3,3,2,5]

def mas_repetida(lista):
    conteo = {}
    for num in lista:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
            
    print(conteo)
    max_count = 0
    frecuente = None
    for num, count in conteo.items():
        if count > max_count:
            max_count = count
            frecuente = num
    return frecuente

    
numero_mas_frecuente = mas_repetida(lista)

print(numero_mas_frecuente)