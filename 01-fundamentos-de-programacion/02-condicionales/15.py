import math

a=float(input("ingrese el termino a del polimonio cuadratico: "))
b=float(input("ingrese el termino b del polinomio cuadratico: "))
c=float(input("ingrese el termino c del polinomio cuadratico: "))
discriminante=(b**2)-(4*a*c)
if discriminante>0:
    x1=round((-b+math.sqrt(discriminante))/(2*a),1)
    x2=round((-b-math.sqrt(discriminante))/(2*a),1)
    print(f"Los valores de las raices reales son x1={x1} y x2={x2}")
elif discriminante==0:
    x=round((-b)/(2*a),1)
    print(f"La raiz real del polinomio es x={x}")
elif discriminante<0:
    x1=round((-b+math.sqrt(abs(discriminante)))/(2*a),1)
    x2=round((-b-math.sqrt(abs(discriminante)))/(2*a),1)
    print(f"Las raices complejas son x1={x1}+i{round(math.sqrt(abs(discriminante)),1)} y x2={x2}-i{round(math.sqrt(abs(discriminante)),1)}")