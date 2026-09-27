n=float(input("Ingrese las horas trabajadas: "))
if n<38:
    tasa=float(input("Ingrese la tasa de remuneracion: "))
    sueldo=n*tasa
    print(f"Su sueldo bruto es de: {sueldo}. Sin impuestos.")
elif n>=38:
    tasa1=float(input("Ingrese la tasa de remuneracion para las primeras 38 horas: "))
    tasa2=float(input("Ingrese la tasa de remuneracion para las horas extras: "))
    sueldo1=38*tasa1
    sueldo2=(n-38)*tasa2
    sueldo=sueldo1+sueldo2
    print(f"Su sueldo bruto es de: {sueldo}. Sin impuestos.")

if sueldo<=450000:
    sueldo_liquido=sueldo*0.98
    print(f"Su sueldo liquido es de: {sueldo_liquido}. Con un 2% de impuesto.")

elif sueldo>450000:
    sueldo_liquido=sueldo*0.95
    print(f"Su sueldo liquido es de: {sueldo_liquido}. Con un 8% de impuesto.")

