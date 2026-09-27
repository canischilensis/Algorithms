"""
Ejercicio
Número perfecto
Un número se dice perfecto, si la suma de todos sus divisores es igual al mismo número (no se debe considerar como divisor al mismo número).
Crea una función llamada numero_perfecto que reciba un número y devuelva True si es un número perfecto, y False en caso de no serlo.
Luego escribe un programa que haga uso de la función para determinar si un número es perfecto o no.
"""
def es_primo(n):
    #Verifica si un número es primo de Mersenne.
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_p(numero):
    """
    Encuentra el valor de p si el número puede ser escrito en la forma 2^(p-1) * (2^p - 1).
    """
    p = 1
    while True:
        mersenne = 2**p - 1
        if es_primo(mersenne):
            numero_perfecto = 2**(p-1) * mersenne
            if numero_perfecto == numero:
                return p
            elif numero_perfecto > numero:
                return None
        p += 1

def es_numero_perfecto(numero):
    """
    Verifica si un número es perfecto utilizando la fórmula de Euclides-Euler.
    """
    p = encontrar_p(numero)
    if p:
        return True
    return False

# Ejemplo de uso
numero = 8128
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
