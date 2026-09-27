import math
r=float(input("Introduzca el radio del cilindro: "))
h=float(input("Introduzca la altura del cilindro: "))
area=round(2*math.pi*r*r,1)
volumen=round(area*h,1)
print(f"el area del circulo es: {area}")
print(f"el volumen del cilindro es: {volumen}")