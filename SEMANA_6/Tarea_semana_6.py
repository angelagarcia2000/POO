# Definición de la clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre  # atributo público
        self.__salario = salario  # atributo privado mediante encapsulación

    # Método público para obtener el salario
    def obtener_salario(self):
        return self.__salario

    # Método para calcular el pago mensual (método que puede ser sobreescrito)
    def calcular_pago(self):
        return self.__salario / 12


# Definición de la clase derivada Gerente que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.__bono = bono  # atributo privado

    # Método para calcular el pago mensual, sobrescribe el método de la clase base
    def calcular_pago(self):
        salario_base = self.obtener_salario()  # Acceso al método encapsulado de la clase base
        return (salario_base + self.__bono) / 12


# Creación de instancias y demostración del programa
if __name__ == "__main__":
    # Creamos una instancia de Empleado
    empleado1 = Empleado("Juan Perez", 50000)
    print(f"Salario de {empleado1.nombre}: ${empleado1.obtener_salario()}")
    print(f"Pago mensual de {empleado1.nombre}: ${empleado1.calcular_pago():.2f}")

    print()  # línea en blanco

    # Creamos una instancia de Gerente
    gerente1 = Gerente("Ana López", 80000, 20000)
    print(f"Salario de {gerente1.nombre}: ${gerente1.obtener_salario()}")
    print(f"Pago mensual de {gerente1.nombre}: ${gerente1.calcular_pago():.2f}")

