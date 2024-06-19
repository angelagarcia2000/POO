# Clase Empleado
class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def obtener_informacion(self):
        return f"Empleado: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento}"

    def aumentar_salario(self, aumento):
        self.salario += aumento
        return f"Nuevo salario de {self.nombre}: ${self.salario}"


# Clase Departamento
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        return f"{empleado.nombre} ha sido agregado al departamento {self.nombre}"

    def calcular_salario_total(self):
        salario_total = sum(empleado.salario for empleado in self.empleados)
        return f"Salario total del departamento {self.nombre}: ${salario_total}"


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear empleados
    emp1 = Empleado("María Pérez", 500, "Ventas")
    emp2 = Empleado("María López", 1000, "TI")
    emp3 = Empleado("Carlos Gómez", 600, "Ventas")

    # Crear departamento
    ventas = Departamento("Ventas")
    ti = Departamento("TI")

    # Agregar empleados a los departamentos
    print(ventas.agregar_empleado(emp1))
    print(ti.agregar_empleado(emp2))
    print(ventas.agregar_empleado(emp3))

    # Aumentar el salario de un empleado
    print(emp1.aumentar_salario(150))

    # Calcular salario total del departamento
    print(ventas.calcular_salario_total())
    print(ti.calcular_salario_total())
