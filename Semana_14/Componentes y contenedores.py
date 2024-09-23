import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de instalar tkcalendar: pip install tkcalendar

class EventManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Eventos")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_lista, columns=("fecha", "hora", "descripcion"), show="headings")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack()

        # Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.entry_fecha = DateEntry(self.frame_entrada)
        self.entry_fecha.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.entry_hora = ttk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.entry_descripcion = ttk.Entry(self.frame_entrada)
        self.entry_descripcion.grid(row=2, column=1)

        # Botones
        self.boton_agregar = ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(pady=5)

        self.boton_salir = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.boton_salir.pack(pady=5)

    def agregar_evento(self):
        """ Agrega un nuevo evento a la lista """
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.entry_hora.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        """ Elimina el evento seleccionado """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?"):
            for item in selected_item:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagerApp(root)
    root.mainloop()
