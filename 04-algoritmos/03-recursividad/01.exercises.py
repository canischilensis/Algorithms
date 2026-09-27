#Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.
def fibonacciR(num):
    if (num==0 or num==1):
        return num
    else:
        return fibonacciR(num-1) + fibonacciR(num-2)
    

if __name__ == "__main__":
    num=int(input("Ingrese el numero de la secuencia: "))
    print(fibonacciR(num))