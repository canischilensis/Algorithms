def linear_search_recursive(lista, indice, elemento,pasos=0):
  print(f"DEBUG: 'elemento:'{elemento}' | 'indice:'{indice}' | 'paso:'{pasos}")
  if indice>=len(lista):
    print(f"El elemento {elemento} no se encontro en la lista.")
    return -1
  if lista[indice]==elemento:
    print(f"El elemento {elemento} se encuentra en la posición {indice}. Se encontró en {pasos} pasos.")
    return indice
  else:
    return linear_search_recursive(lista, indice+1, elemento, pasos+1)

if __name__=="__main__":
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=5
    linear_search_recursive(lista, 0, elemento) #se da el valor del indice 0 que va a ser el lugar donde se inicia
