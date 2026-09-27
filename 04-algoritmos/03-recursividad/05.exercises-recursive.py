#Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano,valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}):
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valores_romanos[romano]
    if valores_romanos[romano[0]] < valores_romanos[romano[1]]:
        return -valores_romanos[romano[0]] + romano_a_decimal(romano[1:])
    else:
        return valores_romanos[romano[0]] + romano_a_decimal(romano[1:])

if __name__ == '__main__':
    assert romano_a_decimal('XXIV')==24
    #print(f'El número romano {numero_romano} en decimal es: {romano_a_decimal(numero_romano)}')