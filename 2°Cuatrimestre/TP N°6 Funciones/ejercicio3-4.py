# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

import math

n = int(input("Ingrese un número entero positivo: "))

def factorial(n):
    if n < 0:
        return "El número debe ser un entero positivo."
    else:
        return math.factorial(n)
    
print("El factorial de",n,"es:",factorial(n))

# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

precio_neto = float(input("Ingrese el precio sin IVA: "))
iva = input("Ingrese el porcentaje de IVA: ")
if iva == "":
    iva = 21

def facturar(precio_neto, iva):
    total = precio_neto + (precio_neto * (iva / 100))
    return total

print("El total de la factura es:", facturar(precio_neto, float(iva)))