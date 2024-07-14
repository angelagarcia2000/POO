#Ejemplo de creación de objetos

class Persona:
    def __init__(self, nombre, edad): #Constructor de la clase persona
                                      #Args:

        self.nombre = nombre          # nombre (str): Nombre de la persona.
        self.edad = edad              # edad (int): Edad de la persona.
        print(f'Se ha creado una nueva persona llamada {self.nombre}')

    def __del__(self):                #Destructor de la clase Persona.

                                      #Se ejecuta cuando el objeto de la clase es destruido,
                                      #lo cual puede suceder cuando el objeto ya no es referenciado
                                      #y el recolector de basura de Python libera la memoria.

        print(f'{self.nombre} ha sido eliminado')


# Crear objetos de la clase Persona
persona1 = Persona('Juan', 30)
persona2 = Persona('María', 25)



# Los objetos persona1 y persona2 se eliminarán automáticamente
# cuando el programa termine, ya que saldrán del ámbito de uso.
