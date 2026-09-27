def to_digito(numero,digito):
    digito=0
    while numero!=0:
        numero = numero//10
        digito = digito+1
    return digito

if __name__=="__main__":
    n=int(input("ingrese numero: "))
    print(to_digito(n,0))