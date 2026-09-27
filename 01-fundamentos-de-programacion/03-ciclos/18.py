n=float(input('ingrese el numero para desarrollar las sumas: '))
acumulador_par=0
acumulador_impar=0
incremento=1
sumador_par=0
sumador_impar=0
contador=0
while acumulador_impar<=n and acumulador_par<=n:
    contador=contador+1
    acumulador_par=contador*2+acumulador_par
    acumulador_impar=(contador*2)-1+acumulador_impar
print(f"la suma de los numeros pares es {acumulador_par}")
print(f"la suma de los numeros impares es {acumulador_impar}")    