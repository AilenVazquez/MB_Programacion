import tkinter as tk
from tkinter import ttk, messagebox

win = tk.Tk()
win.geometry("600x400")
win.title("AGENDA TELEFONICA")
win.iconbitmap("phone.ico")

#------------------FUNCIONES-------------------
def add():
    name = input_name.get()
    phone = input_phone.get()
    if not(name and phone):
        messagebox.showwarning("ADVERTENCIA","Debe ingresar nombre y telefono")
        return
    
    for contact in agenda:
        if name in contact and phone in contact:
            messagebox.showwarning("ADVERTENCIA","El contacto ya existe")
            return
    id = len(agenda)
    agenda.append(["id",name,phone])
    update()
    
def update():
    for elem in tree_agenda.get_children():
        tree_agenda.delete(elem)
    for contact in agenda:
        tree_agenda.insert("","end", values=(contact[0], contact[1],contact[2]))

def remove_selected():
    selected = tree_agenda.selection()
    if selected:
        contact = tree_agenda.item(selected, "values")
        agenda.remove(list(contact))
        tree_agenda.delete(selected)

def update_selected():
    selected = tree_agenda.selection()
    if selected:
        name = input_name.get()
        phone = input_phone.get()
        contact = list(tree_agenda.item(selected, "values"))
        idx = agenda.index(contact)
        agenda[idx] = [contact[0], name, phone]
        update()

#---------------INGRESAR NOMBRE-----------------
label_name = tk.Label(win, text="Nombre:")
label_name.grid(row=0, column=0, pady=5)

input_name = tk.Entry(win)
input_name.grid(row=0, column=1, pady=5)

#--------------INGRESAR TELEFONO----------------
label_phone = tk.Label(win, text="Telefono:")
label_phone.grid(row=0, column=2, pady=5)

input_phone = tk.Entry(win)
input_phone.grid(row=0, column=3, pady=5)


#-----------------BOTON AÑADIR-----------------
btn_add = tk.Button(win, text="AÑADIR",command=add, width=15)
btn_add.grid(row=1, column=0, pady=5)

#-----------------BOTON BORRAR-----------------
btn_remove = tk.Button(win, text="BORRAR",command=remove_selected, width=15)
btn_remove.grid(row=1, column=1, pady=5)

#-----------------BOTON EDITAR-----------------
btn_update = tk.Button(win, text="EDITAR",command=update_selected, width=15)
btn_update.grid(row=1, column=2, pady=5)

#--------------TABLA AGENDA---------------------
tree_agenda = ttk.Treeview(win, columns=("id", "name", "phone"), show="headings")
tree_agenda.grid(row=2, column=0, columnspan=4, pady=5)

tree_agenda.heading("id", text="ID")
tree_agenda.heading("name", text="NOMBRE")
tree_agenda.heading("phone", text="TELEFONO")

tree_agenda.column("id", anchor="center")
tree_agenda.column("name", anchor="center")
tree_agenda.column("phone", anchor="center")

agenda = []

win.mainloop()