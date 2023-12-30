
def area_triangulo(base, altura):
    """Función de cálculo del área del triangulo
    Nos permite calcular el área de un triángulo dados su altura y base

    Args:
        base (float): Base del triángulo en centímetros. Valor positivo.
        altura (float): Altura del triángulo en centímetros. Valor positivo.
    """
    return(round((base * altura / 2),6))

def area_triangulo2(base_altura):
    """Función de cálculo del área del triangulo
    Nos permite calcular el área de un triángulo dados su altura y base
    Múltiples cálculos simultáneos

    Args:
        base_altura (list): lista con los valores de base / altura para cada uno de los triángulos como sublistas de números tipo float.
    """
    return(round((base_altura[0] * base_altura[1] / 2),6))


def volumen_prisma(base, altura1, altura2):
    """ Función de cálculo del volumen del prisma
     Nos permite calcular el volumen de un prisma dados sus alturas y base

    Args:
        base (float): Base del triángulo del prisma en centímetros. Valor positivo.
        altura1 (float): Altura del triángulo del prisma en centímetros. Valor positivo
        altura2 (float): Altura del prisma en centímetros. Valor positivo.
    """
    return(round((base * altura1 * altura2 / 2),6))


def area_cuadrado(lado):
    """# Función de cálculo del área del cuadrado
    # Nos permite calcular el área de un cuadrado dada la longitud de su lado

    Args:
        lado (float): Lado del cuadrado en centímetros. Valor positivo.
    """
    return(round(lado**2, 6))

def volumen_cubo(lado):
    """Función de cálculo del volumen del cubo
    # Nos permite calcular el área de un cubo dada la longitud de su lado

    Args:
        lado (float): Lado del cuadrado en centímetros. Valor positivo.
    """
    return(round(lado**3, 6))


def area_circulo(radio):
    """# Función de cálculo del área del círculo
    # Nos permite calcular el área de un círculo dado su radio

    Args:
        radio (float): Valor del radio de la circunferencia en centímetros. Valor positivo.
    """
    import math
    return(round(math.pi*(radio**2), 6))


def volumen_esfera(radio):
    """# Función de cálculo del volumen de la esfera
    # Nos permite calcular el área de una esfera dado su radio

    Args:
        radio (float): Valor del radio de la circunferencia en centímetros. Valor positivo.
    """
    import math
    return(round(4/3 * math.pi * (radio**3), 6))


def contar(datos):
    """# Función para calcular la longitud de los datos que entran como variable de la función

    Args:
        datos (lista): Lista de datos con los valores de las consultas sucesivas durante la ejecución del proceso

    Returns:
        int: Valor numérico con la longitud del conjunto de datos de entrada
    """
    return len(datos)

def media(datos):
    """Función para calcular la media de los datos de entrada

    Args:
        datos (lista): Lista de datos con los resultados de las consultas sucesivas durante la ejecución del proceso.

    Returns:
        float: Valor de la media calculada de los resultados todas las consultas realizadas para un tipo de consulta durante la sesión.
    """
    from numpy import mean
    return (round(mean(datos), 6))

def minimo(datos):
    """Función para calcular el valor mínimo de los datos de entrada

    Args:
        datos (float): Valor de mínimo de los resultados todas las consultas realizadas para un tipo de consulta durante la sesión.
    """
    return(min(datos))

def maximo(datos):
    """Función para calcular el valor máximo de los datos de entrada

    Args:
        datos (float): Valor de máximo de los resultados todas las consultas realizadas para un tipo de consulta durante la sesión.
    """
    return(max(datos))