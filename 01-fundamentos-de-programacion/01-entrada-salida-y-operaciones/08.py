#input pies (ft)
ft=float(input("ingrese su distancia en pies: "))
#pulgdas (in)
pulgadas=round(ft*12,1)
#centimetros
cm=round(pulgadas*2.54,1)
#metros
m=round(0.01*cm,1)
#print
print(f"su distancia en {ft} ft equivale en pulgadas a {pulgadas} in, en centimetros a {cm} cm y en metros a {m} m.")