
#Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.
def powers(a,b):
    if a==0 and b==0:
        return ("es cero elevado a cero, el valor es indeterminado o tiene un valor de uno. Depende desde donde se vea, si es desde el Cálculo es cero.")
    elif a==0:
        return 0
    elif b==0:
        return 1
    elif a==1 and b==1:
        return 1
    elif b==1:
        return a
    else:
        return a*powers(a,b-1)

if __name__ == "__main__": 
    #base=int(input("ingrese la base de la potencia: "))
    #exponent=int(input("ingrese el exponente de la potencia: "))
    #print(powers(base,exponent))
    assert powers(0,0)=="es cero elevado a cero, el valor es indeterminado o tiene un valor de uno. Depende desde donde se vea, si es desde el Cálculo es cero."
    assert powers(0,1)==0
    assert powers(234,0)==1
    assert powers(234,1)==234
    assert powers(234,2)==54756
    assert powers(2,3)==8