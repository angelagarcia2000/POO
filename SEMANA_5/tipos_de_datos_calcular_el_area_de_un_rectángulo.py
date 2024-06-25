# Programa para calcular el área de un rectángulo
# Utiliza diferentes tipos de datos y sigue convenciones de identificación

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dado su base y altura.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área calculada del rectángulo.
    """
    area = base * altura
    return area

# Datos de prueba
base_rectangulo = 5.2
altura_rectangulo = 3.8

# Calcular el área del rectángulo
area_del_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Imprimir el resultado
print(f"El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es: {area_del_rectangulo}")
