import os
# Importa el módulo os para interactuar con el sistema operativo

# Función para mostrar el contenido de un archivo
def mostrar_codigo(ruta_script):
    # Convierte la ruta del script a una ruta absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Abre el archivo en modo lectura
        with open(ruta_script_absoluta, 'r') as archivo:
            # Imprime el nombre del archivo y su contenido
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        # Si el archivo no se encuentra, imprime un mensaje de error
        print("El archivo no se encontró.")
    except Exception as e:
        # Si ocurre cualquier otro error, imprime el error
        print(f"Ocurrió un error al leer el archivo: {e}")

# Función para mostrar el menú y manejar las elecciones del usuario
def mostrar_menu():
    # Obtiene la ruta del directorio donde se encuentra el script principal
    ruta_base = os.path.dirname(__file__)

    # Diccionario con las opciones del menú y sus rutas correspondientes
    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-1. Ejemplo Programacion tradicional frente a POO.py',
        '3': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-2. Ejemplo No. 02 - POO.py',
        '4': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-2. Ejemplo No. 02 - Programacion tradicional.py',
        '5': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-3. Tarea Programacion OO.py',
        '6': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-3. Tarea Programacion Tradicional.py',
        '7': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-1. Ejemplo - Carro y Acciones.py',
        '8': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-2. Ejemplo - Carro Relacion Persona.py',
        '9': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-3. Ejemplo - Print Atributos Clase.py',
        '10': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-4. Ejemplo - Libro, Bibliotecario y Usuario.py',
        '11': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-5. Ejemplo - Libro, Persona y Rol.py',
        '12': 'Unidad 2/1.1. Tipos de Datos e Identificadores/2.1.1-1 - Nomenclatura en Python.py',
        '13': 'Unidad 2/1.1. Tipos de Datos e Identificadores/2.1.1-2 - Ejemplo Identificadores correctos (Python).py',
        '14': 'Unidad 2/1.1. Tipos de Datos e Identificadores/2.1.1-3 - Ejemplo Identificadores poco claros (Python).py',
        '15': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-1 - Ejemplo Clase y Objeto (Coche).py',
        '16': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-1 - Ejemplo Clase y Objeto (Libro).py',
        '17': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-2 - Ejemplo Herencia (Coche).py',
        '18': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-2 - Ejemplo Herencia Extendido (Coche-Vehiculo).py',
        '19': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-3 - Ejemplo Encapsulación (Cuenta Bancaria).py',
        '20': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-4 - Ejemplo Polimorfismo (Sobrecarga).py',
        '21': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-4 - Ejemplo Polimorfismo (Sobreescritura).py',

    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {os.path.basename(opciones[key])}")
        print("0 - Salir")

        # Solicita al usuario que elija una opción
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            # Si el usuario elige '0', se sale del bucle y termina el programa
            break
        elif eleccion in opciones:
            # Si el usuario elige una opción válida, obtiene la ruta del script correspondiente
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            # Muestra el código del script seleccionado
            mostrar_codigo(ruta_script)
        else:
            # Si la opción no es válida, imprime un mensaje de error
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecuta el menú si el script se está ejecutando directamente
if __name__ == "__main__":
    mostrar_menu()


