import math
a=float(input("Ingrese un lado del triangulo: "))
b=float(input("Ingrese el segundo lado del triangulo: "))
c=float(input("Ingrese el tercer del triangulo: "))
p=(a+b+c)/2
area=round((p*(p-a)*(p-b)*(p-c))**0.5)
print(f"El area del triangulo es: {area}")