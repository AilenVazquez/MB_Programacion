import random
numero_secreto = random.randint(1, 10)

intentos = 0

while intentos < 3:
    intento = int(input("Adivina un numero del 1 al 10: "))
    if intento == numero_secreto:
        print("Correcto, adivinaste el numero")
        break
    else:
        print("Incorrecto, intenta de nuevo")
        intentos +=1