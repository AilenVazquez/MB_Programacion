# print("Hola Mundo")

# a = 5
# b= 3.14
# c= "Hola"

# luz = False12
# if luz == True:
#     print("La luz esta prendida")
# else:
#     print("La luz esta apagada")

numero1 = int(input("Ingrese el primer numero: "))
operacion = input("Ingrese la operacion a realizar: ")
numero2 = int(input("Ingrese el segundo numero: "))

if operacion == "+":
    print(numero1+numero2)
elif operacion == "-":
    print(numero1-numero2)
elif operacion == "*" or "x":
    print(numero1*numero2)
elif operacion == "/":
    print(numero1/numero2)
