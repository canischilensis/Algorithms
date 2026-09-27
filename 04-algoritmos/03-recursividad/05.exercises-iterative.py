#Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):
    valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    previo = 0

    for letra in romano[::-1]:
        valor = valores_romanos[letra]
        if valor < previo:
            decimal -= valor
        else:
            decimal += valor
        previo = valor

    return decimal

if __name__ == '__main__':
    assert romano_a_decimal('XXIV')==24
    #print(f'El número romano {numero_romano} en decimal es: {romano_a_decimal(numero_romano)}')