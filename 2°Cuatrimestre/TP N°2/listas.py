# append agrega un elemento a la lista

productos = ["celular", "laptop", "lapiz", "mochila"]

productos.append("borrador")

productos[1] = "pc"

del productos[-1] #eliminamos el ultimo elemento de la lista

for producto in productos:
    print(f"-{producto}")
    
productos.reverse() #Da vuelta la lista

for producto in productos:
    
    print(f"-{producto}")