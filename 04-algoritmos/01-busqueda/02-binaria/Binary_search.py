def binary_search(lista, elemento):
    der=len(lista)-1
    izq=0
    pasos=0
    encontrado=False
    while izq<=der:
        pasos+=1
        medio=(der+izq)//2
        encontrado=True
        print(f"DEBUG1: 'derecha: {der}' | 'izquierda: {izq}' | pasos: {pasos}' | 'medio: {medio}' | 'elemento: {elemento}'")
        if lista[medio]==elemento:
            print(f"elemento {elemento} se encuentra en la posicion {medio}, el algoritmo lo ubico en {pasos} pasos")
            encontrado= True
            break
        elif lista[medio]>elemento:
            der=medio-1
            print(f"DEBUG2: 'izquierda: {izq}' | 'el valor de la derecha se cambia a: {der}' | 'pasos: {pasos}' | 'elemento {elemento}'")
        elif lista[medio]<elemento:
            izq=medio+1
            print(f"DEBUG2: 'el valor de la izquierda se cambia a: {izq}' | 'derecha: {der}' | 'pasos: {pasos}' | 'elemento {elemento}'")
    if encontrado==False:
        print(f"el elemento {elemento} no esta en la lista")  

if __name__ == "__main__":
    lista=[1,3,5,7,9,11,13,15,17,19,21,23]
    elemento=5
    binary_search(lista, elemento)