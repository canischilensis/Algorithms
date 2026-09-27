import math

def jump_search_recursive(lista, elemento, step=0, last_index=0):
    if step == 0:
        step = math.sqrt(len(lista))

    if last_index >= len(lista):
        return -1

    if lista[int(min(step, len(lista) - 1))] >= elemento:
        return linear_search(lista, elemento, int(max(0, last_index - step)), int(last_index))

    return jump_search_recursive(lista, elemento, step + math.sqrt(len(lista)), last_index)

def linear_search(lista, elemento, start, end):
    if start >= len(lista) or lista[start] > elemento:
        return -1

    if lista[start] == elemento:
        return start

    return linear_search(lista, elemento, start + 1, end)

if __name__ == '__main__':
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 21
    result = jump_search_recursive(lista, elemento)
    
    if result != -1:
        print(f'Valor encontrado en la posición {result}')
    else:
        print('Valor no encontrado')
