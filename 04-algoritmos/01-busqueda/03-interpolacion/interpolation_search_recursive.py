from time import perf_counter

def interpolation_search_recursive(arr, e, i=0, j=None, step=0):
    if j is None:
        j = len(arr) - 1
    encontrado = False
    if i == j:
        if arr[i] == e:
            print(f'Valor encontrado en {step} step, en la posicion {i}')
            return i
        else:
            print(f'El elemento {e} no esta en la lista')
            return -1
    if arr[j] != arr[i] and arr[i] <= e <= arr[j]:
        step += 1
        pos = i + ((e - arr[i]) * (j - i) // (arr[j] - arr[i]))
        print(f"DEBUG: 'low: {i}' | 'high: {j}' | 'posicion: {pos} | 'step: {step}' ")
        if e == arr[pos]:
            print(f'Valor encontrado en {step} step, en la posicion {pos}')
            encontrado = True
            return pos
        elif e > arr[pos]:
            print(f"DEBUG Si el {e} es menor que {pos}: |'low: {i}' | 'el valor de {i} cambia a {pos+1}' | 'pasos: {step}' | 'elemento {e}'")
            return interpolation_search_recursive(arr, e, pos+1, j, step)
        else:
            print(f"DEBUG Si el {e} es mayor que {pos}: 'high: {i}' | 'el valor de {j} cambia a {pos-1}' | 'pasos: {step}' | 'elemento {e}'")
            return interpolation_search_recursive(arr, e, i, pos-1, step)
    if not encontrado:
        print(f'El elemento {e} no esta en la lista')
        return -1

if __name__ == '__main__':
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=11
    start_time=perf_counter()
    interpolation_search_recursive(lista, elemento)
    end_time=perf_counter()
    elapsed_ms = (end_time - start_time) * 1000  # milisegundos
    print(f"⏱️ Tiempo de ejecución: {elapsed_ms:.4f} ms")