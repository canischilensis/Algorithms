contador=0
acumulador=0
sumador=0
while sumador!=99:
    sumador=float(input('Ingrese el numero que quiere sumar: '))
    acumulador=sumador+acumulador
    contador=contador+1

print(f'la cantidad de nuermos que se introdujeron fue de:{contador-1}')
print(f'La suma de los numeros introducidos es de:{acumulador-99}')