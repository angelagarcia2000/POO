
#Programa para realizar construcción de objetos.
class Animal:
    def __init__(self, gato):
        """Constructor que inicializa el objeto y abre el archivo."""
        self.gato = gato
        self.file = open(gato, 'w')  # Abrimos el archivo en modo escritura

    def write_data(self, data):
        """Método para escribir datos en el archivo."""
        self.file.write(data)

    def __del__(self):
        """Destructor que se activa cuando el objeto es eliminado."""
        if hasattr(self, 'file'):
            self.file.close()  # Cerramos el archivo si aún está abierto
            print(f"Archivo '{self.gato}' cerrado correctamente.")


# Ejemplo de uso de la clase Animal
if __name__ == "__main__":
    # Creamos una instancia de Animal
    handler = Animal("gato")

    # Escribimos datos en el archivo
    handler.write_data("Hola, mundo!\n")
    handler.write_data("Este es un ejemplo de uso de constructores y destructores en Python.\n")

    # No necesitamos cerrar explícitamente el archivo, el destructor lo hará automáticamente al eliminar el objeto
    # Sin embargo, podemos eliminar la referencia al objeto para forzar la llamada al destructor
    del handler
