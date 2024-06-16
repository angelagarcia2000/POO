# Implementación en Programación Tradicional

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Función principal
def main():
    print("Bienvenido al programa de cálculo de promedio semanal del clima.")

    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)

    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius.")


# Llamada a la función principal
if __name__ == "__main__":
    main()
