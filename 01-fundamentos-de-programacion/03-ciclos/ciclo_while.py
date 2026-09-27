#logica de un sumador
contador=0 #para contar los numeros
sumador=0 #para sumar los numeros
n=1
#captura de datos y procesamiento
while (n!=0):
    n=int(input("Indique un numero: "))
    if n!=0:
        contador=contador+1
        sumador=sumador+n
    else:
        print("Cantidad de numeros",contador)
        print("Suma de los numeros",sumador)


