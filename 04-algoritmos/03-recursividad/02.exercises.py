#Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.

def sum_recursive(num):
    if num==0:
        return 0
    else:
        return num + sum_recursive(num-1)


if __name__ == "__main__":
    num=int(input("Ingrese el numero positivo: "))
    print(sum_recursive(num))