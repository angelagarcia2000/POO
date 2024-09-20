import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para agregar dato a la tabla
def agregar_dato():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    edad = entrada_edad.get()
    if nombre and apellido and edad.isdigit():
        tabla_de_datos.insert("", tk.END, values=(nombre, apellido, edad))
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Datos inválidos", "Por favor ingrese datos válidos. Asegúrese de que la edad sea un número.")

# Función para limpiar la tabla
def limpiar_tabla():
    for item in tabla_de_datos.get_children():
        tabla_de_datos.delete(item)

# Creación de la ventana o interfaz gráfica
ventana = tk.Tk()
ventana.title("Sistema de Registro")
ventana.config(bg="antique white")
ventana.geometry("600x600")

# Etiqueta y campo de entrada para el nombre
label_nombre = tk.Label(ventana, text="Ingrese su Nombre: ", bg="antique white")
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=25)
entrada_nombre.pack()

# Etiqueta y campo de entrada para el apellido
label_apellido = tk.Label(ventana, text="Ingrese su Apellido: ", bg="antique white")
label_apellido.pack(pady=5)
entrada_apellido = tk.Entry(ventana, width=25)
entrada_apellido.pack()

# Etiqueta y campo de entrada para la edad
label_edad = tk.Label(ventana, text="Ingrese su Edad: ", bg="antique white")
label_edad.pack(pady=5)
entrada_edad = tk.Entry(ventana, width=25)
entrada_edad.pack()

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", bg="blue", fg="white", command=agregar_dato)
boton_agregar.pack(pady=10)

# Tabla para mostrar los datos
tabla_de_datos = ttk.Treeview(ventana, columns=("Nombre", "Apellido", "Edad"), show="headings")
tabla_de_datos.heading("Nombre", text="Nombre")
tabla_de_datos.heading("Apellido", text="Apellido")
tabla_de_datos.heading("Edad", text="Edad")

tabla_de_datos.column("Nombre", anchor="center", width=150)
tabla_de_datos.column("Apellido", anchor="center", width=150)
tabla_de_datos.column("Edad", anchor="center", width=100)

tabla_de_datos.pack(pady=20)

# Botón para limpiar la tabla
boton_limpiar = tk.Button(ventana, text="Limpiar", bg="blue", fg="white", command=limpiar_tabla)
boton_limpiar.pack(pady=10)

ventana.mainloop()
