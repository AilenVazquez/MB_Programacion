import math

cat1 = int(input("Ingrese el cateto 1: "))
cat2 = int(input("Ingrese el cateto 2: "))

hipotenusa = int(math.sqrt(pow(cat1, 2) + pow(cat2,2)))

print("La hipotenusa es: ", hipotenusa)