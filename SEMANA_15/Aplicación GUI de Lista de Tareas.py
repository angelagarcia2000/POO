#  Desarrollar una aplicación GUI simple para gestionar una lista de tareas, permitiendo al usuario añadir nuevas tareas,
#  marcarlas como completadas y eliminarlas. La aplicación deberá responder adecuadamente a los eventos del usuario,
#  como clics del ratón y pulsaciones del teclado.


import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Frame para la entrada de tareas y botones
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.pack(side=tk.LEFT)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Vincular la tecla Enter a la función de añadir tarea
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Vincular doble clic en la tarea para marcar como completada
        self.task_listbox.bind('<Double-Button-1>', lambda event: self.complete_task())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            # Añadir "✓" al inicio de la tarea para marcarla como completada
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, "✓ " + task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

