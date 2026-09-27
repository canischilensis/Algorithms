#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def decimal_to_binary(decimal):
    if decimal==0:
        return '0'
    elif decimal==1:
        return '1'
    else:
        return decimal_to_binary(decimal//2)+str(decimal%2)
    
if __name__ == "__main__":
    #decimal=int(input("Ingrese el numero decimal: "))
    #print(decimal_to_binary(decimal))
    assert decimal_to_binary(1)=='1'
    assert decimal_to_binary(0)=='0'
    assert decimal_to_binary(2)=='10'
    assert decimal_to_binary(24)=='11000'