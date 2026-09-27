contador=1
acumulador=0
multiplicador=2
incremento=1
numero=float(input('ingrese el numero natural para identificar los numeros pares:'))
while numero>acumulador:
    acumulador=contador*multiplicador
    contador=contador+incremento
    print(f'el numero par es: {acumulador}')


