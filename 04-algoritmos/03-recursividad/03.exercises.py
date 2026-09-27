#Implementar una función para calcular el producto de dos números enteros dados.
def product(a,b):
    if a==0 or b==0:
        return 0
    elif a==0:
        return b
    elif b==0:
        return a
    else:
        return a+product(a,b-1)

if __name__ == "__main__": 
    input=int(input("inserte un factor: "))
    input2=int(input("inserte otro factor: "))
    print(product(input,input2))