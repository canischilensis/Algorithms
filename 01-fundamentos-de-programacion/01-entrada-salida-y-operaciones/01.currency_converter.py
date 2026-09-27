CLP=input("How many CLP do you have? ")
CLP=float(CLP)
valor_USD=801
USD=CLP/801
USD=round(USD,2)
USD=str(USD)
print("Tienes $"+USD+"USD")

#convertir dolares a pesos
USD=input("How many dollars do you have? ")
USD=float(USD)
valor_USD=801
CLP=USD+valor_USD
CLP=round(CLP,2)
CLP=str(CLP)

print("Tienes $"+CLP+"CLP ")
