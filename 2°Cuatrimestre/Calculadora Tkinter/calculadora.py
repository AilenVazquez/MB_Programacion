import tkinter as tk

win = tk.Tk()
win.title("CALCULADORA")
win.geometry("400x300")
win.iconbitmap("calculadora.ico")


def sumar():
    suma = float(input_numero1.get()) + float(input_numero2.get())
    label_resuldato.config(text=f"El resultado es: {suma}")
    limpiar()
    
def restar():
    resta = float(input_numero1.get()) - float(input_numero2.get())
    label_resuldato.config(text=f"El resultado es: {resta}")
    limpiar()

def multiplicar():
    multilicacion = float(input_numero1.get()) * float(input_numero2.get())
    label_resuldato.config(text=f"El resultado es: {multilicacion}")
    limpiar()  

def dividir():
    num1 = float(input_numero1.get())
    num2 = float(input_numero2.get())
    if num2 == 0:
        label_resuldato.config(text="Error: No es posible dividir por cero")
        limpiar()
        return
    else:
        division = num1 / num2
        label_resuldato.config(text=f"El resultado es: {division}")
        limpiar()  
    
def limpiar():
    input_numero1.delete(0, tk.END)
    input_numero2.delete(0, tk.END)

#-----------------PRIMER NUMERO-----------------
label_numero1 = tk.Label(win, text="Ingrese un número:", font=("Arial", 16))
label_numero1.pack()
input_numero1 = tk.Entry(win,borderwidth=2)
input_numero1.pack()

#-----------------SEGUNDO NUMERO-----------------
label_numero2 = tk.Label(win, text="Ingrese otro número:", font=("Arial", 16))
label_numero2.pack()
input_numero2 = tk.Entry(win,borderwidth=2)
input_numero2.pack()

#---------------------BOTONES---------------------

# Crear los dos botones de arriba
frame_superior = tk.Frame(win)
frame_superior.pack(pady=10) # Añade espacio vertical

#--------------SUMAR--------------
btn_suma = tk.Button(frame_superior, text="+", command=sumar, width=10, font=("Arial", 14), borderwidth=5)
btn_suma.pack(side=tk.LEFT, padx=5)

#--------------RESTAR--------------
btn_resta = tk.Button(frame_superior, text="-", command=restar, width=10, font=("Arial", 14), borderwidth=5)
btn_resta.pack(side=tk.LEFT, padx=5)


# Crear los dos botones de abajo
frame_inferior = tk.Frame(win)
frame_inferior.pack(pady=10) # Añade espacio vertical

#------------MULTIPLICAR-----------
btn_multiplicar = tk.Button(frame_inferior, text="X", command=multiplicar, width=10, font=("Arial", 14), borderwidth=5)
btn_multiplicar.pack(side=tk.LEFT, padx=5)

#-------------DIVIDIR--------------
btn_dividir = tk.Button(frame_inferior, text="/", command=dividir, width=10, font=("Arial", 14), borderwidth=5)
btn_dividir.pack(side=tk.LEFT, padx=5)



#--------------------RESULTADO--------------------
label_resuldato = tk.Label(win, text="El resultado es:", font=("Arial", 16))
label_resuldato.pack()



win.mainloop()