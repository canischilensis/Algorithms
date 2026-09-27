#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def decimal_to_binary(decimal):
    binary=''
    if decimal==0:
        return '0'
    while decimal>0:
        remainder=decimal%2
        binary=str(remainder)+binary
        decimal= decimal//2
    return binary
    
if __name__ == "__main__":
    #decimal=int(input("Ingrese el numero decimal: "))
    #print(decimal_to_binary(decimal))
    assert decimal_to_binary(1)=='1'
    assert decimal_to_binary(0)=='0'
    assert decimal_to_binary(2)=='10'
    assert decimal_to_binary(24)=='11000'