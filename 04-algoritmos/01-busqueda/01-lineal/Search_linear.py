def linear_search(lista, elemento):
    posicion = 0
    pasos=0
    encontrado=0
    while posicion < len(lista):
        pasos+=1
        print(f"DEBUG: 'elemento:{elemento}' | 'posicion:{posicion}' | 'pasos:{pasos}'")
        if lista[posicion] == elemento:
            print(f"se ha encontrado el {elemento} en la posicion {posicion}, en {pasos} pasos")
        elif posicion == len(lista):
            print(f"el elemento {elemento} no fue encontrado en la lista")
        posicion+=1

if __name__ == '__main__':
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=5
    linear_search(lista, elemento)
