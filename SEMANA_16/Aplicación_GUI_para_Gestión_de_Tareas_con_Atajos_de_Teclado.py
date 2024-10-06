#  Desarrollar una aplicación GUI que permita a los usuarios gestionar una lista de tareas pendientes.
#  La aplicación deberá permitir añadir nuevas tareas, marcar tareas como completadas,
#  y eliminar tareas utilizando tanto la interfaz gráfica (clics de botón) como atajos de teclado.

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Crear campo de entrada para añadir tareas
        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())  # Atajo de teclado Enter para añadir tarea

        # Crear botón para añadir tarea
        self.add_button = tk.Button(self.root, text="Añadir tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Crear lista para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=15, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botones para marcar como completada y eliminar
        self.complete_button = tk.Button(self.root, text="Marcar como completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

        # Vincular atajos de teclado
        self.root.bind("<c>", lambda event: self.complete_task())  # Atajo 'C' para marcar como completada
        self.root.bind("<d>", lambda event: self.delete_task())  # Atajo 'D' para eliminar
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Atajo 'Delete' para eliminar
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Atajo 'Esc' para cerrar la app

        # Lista para guardar las tareas
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo de tarea está vacío")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Advertencia", "No hay ninguna tarea seleccionada")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Advertencia", "No hay ninguna tarea seleccionada")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["text"]
            if task["completed"]:
                self.task_listbox.insert(tk.END, f"[Completada] {task_text}")
            else:
                self.task_listbox.insert(tk.END, task_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
