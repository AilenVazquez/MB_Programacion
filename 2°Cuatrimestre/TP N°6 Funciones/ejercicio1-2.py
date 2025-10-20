# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludar():
    print("!Hola amiga!")
    
    
saludar()

# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

nombre = input("Ingrese su nombre: ")

def saludo(nombre):
    print("! Hola", nombre,"!")
    
saludo(nombre)