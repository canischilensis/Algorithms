def to_digito(numero,digito):
    if numero!=0:
        return to_digito(numero//10,digito+1)
    else:
        return digito

if __name__=="__main__":
    n=int(input("ingrese numero: "))
    print(to_digito(n,0))