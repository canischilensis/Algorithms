menu="""
Welcome to currency converter module
Select number your option to converter:

1. colombian pesos COP
2. argentinian pesos ARP
3. mexicanan pesos MXN

enter your number option:

"""
option=int(input(menu))
if option==1:
    COP=input("How many COP do you have?")
    COP=float(COP)
    valor_USD=4428
    USD=COP/valor_USD
    USD=round(USD,2)
    USD=str(USD)
    print('Tienes $ '+USD+' USD')

elif option==2:
    ARP=input("How many ARP do you have?")
    ARP=float(ARP)
    valor_USD=217
    USD=ARP/valor_USD
    USD=round(USD,2)
    USD=str(USD)
    print('Tienes $ '+USD+' USD')

elif option==3:
    MXN=input("How many MXN do you have?")
    MXN=float(MXN)
    valor_USD=18
    USD=MXN/valor_USD
    USD=round(USD,2)
    USD=str(USD)
    print('Tienes $ '+USD+' USD')
