import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def agregar_dato():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    edad = entrada_edad.get()
    if nombre and apellido and edad.isdigit():
        tabla_de_datos.insert(tk.END, values=(nombre, apellido, edad))
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Porfavor ingrese los datos")


def limpiar_dato():
    for item in tabla_de_datos.get_children():
        tabla_de_datos.delete(item)


ventana = tk.Tk()
ventana.title("Sistema de Registro")
ventana.config(bd = "yellow")
ventana.geometry(600*600)

style = ttk.Style()
style.configure("Treeview", anchor="center")
style.configure("Treeview", rowheight=25)
style.configure("mystyle", anchor="center")

label_nombre = tk.Label(ventana, text="Ingrese su Nombre: ")
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=25)
entrada_nombre.pack

label_apellido = tk.Label(ventana, text="Ingrese su Apellido: ")
label_apellido.pack(pady=4)
entrada_apellido = tk.Entry(ventana, width=30)
entrada_apellido.pack

label_edad = tk.Label(ventana, text="Ingrese su Edad: ")
label_edad.pack(pady=4)
entrada_edad = tk.Entry(ventana, width=30)
entrada_edad.pack

boton_agregar = tk.Button(ventana,
                          text="agregar",
                          bg="blue",
                          command=agregar_dato)
boton_agregar.pack(pady=8)

tabla_de_datos = ttk.Treeview(ventana, columns=("Nombre", "Apellido", "Edad"), show="headings",
                              style="mystyle.Treeview")
tabla_de_datos.heading("Nombre", text="Nombre")
tabla_de_datos.heading("Apellido", text="Apellido")
tabla_de_datos.heading("Edad", text="Edad")

tabla_de_datos.column("Nombre", anchor="center", width=90)
tabla_de_datos.column("Apellido", anchor="center", width=90)
tabla_de_datos.column("Edad", anchor="center", width=90)

boton_limpiar = tk.Button(ventana,
                          text="limpiar",
                          bg="blue",
                          command=limpiar_dato)

boton_limpiar.pack(pady=8)
ventana.mainloop()
