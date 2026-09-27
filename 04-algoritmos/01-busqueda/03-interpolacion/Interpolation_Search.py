from time import perf_counter

def interpolation_search(arr,e):
    i=0
    j=len(arr)-1
    pos=0
    step=0
    if i == j:
      if arr[i] == e:
          print(f"elemento {e} se encuentra en la posicion {i}, el algoritmo lo ubico en {step} pasos")
          return i
      else:
          print(f"El elemento {e} no esta en la lista")
          return -1
    while i <= j and e >= arr[i] and e <= arr[j]:
      pos= i + (((e-arr[i])*(j-i))//(arr[j]-arr[i]))
      print(f"DEBUG: 'low: {i}' | 'high: {j}' | 'posicion: {pos} | 'pasos: {step}' ")
      step += 1
      if arr[pos] == e:
        print(f"elemento {e} se encuentra en la posicion {pos}, el algoritmo lo ubico en {step} pasos")
        print(f"DEBUG El elemento {e} esta en la poscion {pos}: |'low: {i}' | 'high: {j}' | 'pasos: {step}' | 'elemento {e}'")
        encontrado=True
        return pos
      elif arr[pos] < e:
        print(f"DEBUG Si el {e} es menor que {pos}: |'low: {i}' | 'el valor de {i} cambia a {pos+1}' | 'pasos: {step}' | 'elemento {e}'")
        i=pos+1
      else:
        print(f"DEBUG Si el {e} es mayor que {pos}: 'high: {i}' | 'el valor de {j} cambia a {pos-1}' | 'pasos: {step}' | 'elemento {e}'")
        j=pos-1

if __name__ == "__main__":
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=11
    start_time=perf_counter()
    interpolation_search(lista, elemento)
    end_time=perf_counter()
    elapsed_ms = (end_time - start_time) * 1000  # milisegundos
    print(f"⏱️ Tiempo de ejecución: {elapsed_ms:.4f} ms")