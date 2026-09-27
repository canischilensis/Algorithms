def exponential_search(lista, elemento):
    if lista[0]==elemento:
        return 0
    bound = 1

    while bound<len(lista) and lista[bound]<=elemento:
        bound*=2
    print(f"DEBUG: 'bound:'{bound}' | 'elemento:'{elemento}'")
    return binary_search(lista, elemento, bound//2, min(bound,len(lista)-1))

def binary_search(lista, elemento, left, right):
    pasos=0
    encontrado=False
    while left<=right:
        pasos+=1
        medio=(right+left)//2
        print(f"DEBUG: 'rightecha: {right}' | 'leftuierda: {left}' | pasos: {pasos}' | 'medio: {medio}' | 'elemento: {elemento}'")
        encontrado=True
        if lista[medio]==elemento:
            print(f"elemento {elemento} se encuentra en la posicion {medio}, el algoritmo lo ubico en {pasos} pasos")
            encontrado= True
            break
        elif lista[medio]>elemento:
            right=medio-1
            print(f"DEBUG: 'left: {left}' | 'el valor de la rightecha se cambia a: {right}' | 'pasos: {pasos}' | 'elemento {elemento}'")
        elif lista[medio]<elemento:
            left=medio+1
            print(f"DEBUG: 'el valor de left se cambia a: {left}' | 'right: {right}' | 'pasos: {pasos}' | 'elemento {elemento}'")
    if not encontrado:
        print(f"el elemento {elemento} no esta en la lista")

if __name__ == '__main__':
    lista = [1,3,5,7,9,11,13,15,17,19,21,23]
    elemento = 3
    exponential_search(lista, elemento)
