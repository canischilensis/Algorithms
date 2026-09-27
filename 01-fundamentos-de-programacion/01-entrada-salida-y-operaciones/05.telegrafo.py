"""
Ejercicio

Telégrafo

Dado un mensaje, se debe calcular su costo para enviarlo por telégrafo. Para esto se sabe que cada letra cuesta $10, 
los caracteres especiales que no sean letras cuestan $30 y los dígitos tienen un valor de $20 cada uno. 
Los espacios no tienen valor. Su mensaje debe ser un string, y las letras del castellano (ñ, á, é, í, ó, ú) 
se consideran caracteres especiales. 
Escriba una función que permita calcular el costo de un mensaje.
"""
def costo_mensaje(mensaje):
    costo = 0
    # Lista de caracteres especiales
    caracteres_especiales = ['ñ', 'á', 'é', 'í', 'ó', 'ú', 'Ñ', 'Á', 'É', 'Í', 'Ó', 'Ú', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
    # Lista de números
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for valor in mensaje:
        if valor in numeros:
            costo += 20
        elif valor in caracteres_especiales:
            costo += 30
        elif valor == " ":
            costo += 0
        else:
            costo += 10
    return costo

if __name__ == '__main__':
    mensaje =input("Ingrese el mensaje:")
    print(f"Costo del mensaje: ${costo_mensaje(mensaje)}")
    op=input("Ejecutar otra vez? S?N: ").upper()