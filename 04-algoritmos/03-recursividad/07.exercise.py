#Desarrollar un algoritmo que permita calcular la siguiente serie:
#h(n)=1+1/2+1/3+1/4...1/n
def h(n):
    if n==1:
        return 1
    elif n!=0:
        return round(1/n + h(n-1), 2)

if __name__ == "__main__":
    assert h(1)==1.00
    assert h(2)==1.50
    assert h(3)==1.83
    assert h(4)==2.08
    assert h(5)==2.28