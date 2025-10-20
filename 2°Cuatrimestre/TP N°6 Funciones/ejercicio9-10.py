# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

import math

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

def min_com_div(num1, num2):
    maximo = math.gcd(num1, num2)
    return maximo

def max_com_mul(num1, num2):
    minimo = math.lcm(num1,num2)
    return minimo

print(f"El máximo común divisor de {num1} y {num2} es: {min_com_div(num1, num2)}")
print(f"El mínimo común múltiplo de {num1} y {num2} es: {max_com_mul(num1, num2)}")

# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

conv_bin = int(input("Ingrese un número decimal: "))

def dec_bin(conv_bin):
    numero_binario = bin(conv_bin).replace("0b", "")
    return f"El número decimal {conv_bin} es igual a {numero_binario} en binario."

print(dec_bin(conv_bin))



conv_dec = int(input("Ingrese un número binario: "))

def bin_dec(conv_dec):
    decimal = int(str(conv_dec), 2)
    return f"El número binario {conv_dec} es igual a {decimal} en decimal."

print(bin_dec(conv_dec))