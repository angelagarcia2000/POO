class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Utilizamos tuplas para título y autor ya que son inmutables
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, categoria={self.categoria}, isbn={self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        return self.libros_prestados

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, id_usuario={self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave
        self.usuarios = set()  # Conjunto de IDs de usuario únicos

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)

    def dar_baja_usuario(self, id_usuario):
        self.usuarios = {u for u in self.usuarios if u.id_usuario != id_usuario}

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros:
            libro = self.libros[isbn]
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if usuario:
                usuario.prestar_libro(libro)
                return f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}."
            else:
                return "Usuario no registrado."
        else:
            return "Libro no disponible."

    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros:
            libro = self.libros[isbn]
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if usuario:
                usuario.devolver_libro(libro)
                return f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}."
            else:
                return "Usuario no registrado."
        else:
            return "Libro no disponible."

    def buscar_libro(self, criterio, valor):
        resultado = []
        for libro in self.libros.values():
            if (criterio == 'titulo' and valor.lower() in libro.titulo.lower()) or \
               (criterio == 'autor' and valor.lower() in libro.autor.lower()) or \
               (criterio == 'categoria' and valor.lower() in libro.categoria.lower()):
                resultado.append(libro)
        return resultado

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            return usuario.listar_libros_prestados()
        else:
            return "Usuario no registrado."

    def __repr__(self):
        return f"Biblioteca(libros={self.libros}, usuarios={self.usuarios})"


# Pruebas del sistema

# Crear una biblioteca
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "1234567890")
libro2 = Libro("1984", "George Orwell", "Distopía", "0987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "u001")
usuario2 = Usuario("Ana Gómez", "u002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
print(biblioteca.prestar_libro("1234567890", "u001"))  # Debería ser exitoso
print(biblioteca.prestar_libro("0987654321", "u002"))  # Debería ser exitoso

# Listar libros prestados
print(usuario1.listar_libros_prestados())  # Debería mostrar "El Principito"
print(usuario2.listar_libros_prestados())  # Debería mostrar "1984"

# Devolver libros
print(biblioteca.devolver_libro("1234567890", "u001"))  # Debería ser exitoso

# Buscar libros
print(biblioteca.buscar_libro('titulo', "1984"))  # Debería mostrar "1984"
print(biblioteca.buscar_libro('autor', "Saint-Exupéry"))  # Debería mostrar "El Principito"
print(biblioteca.buscar_libro('categoria', "Distopía"))  # Debería mostrar "1984"

# Listar libros prestados después de devolver
print(usuario1.listar_libros_prestados())  # Debería estar vacío ahora
