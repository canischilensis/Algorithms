#este archivo sirve para ver como estan los codigos en los archivos
import gates

def system(val1,val2,val3):
    circuit_1=gates.logic_and(gates.logic_or(val1,val2),gates.logic_not(val3))
    #circuit_2=gates.logic_and(gates.logic_not)
    #S = [circuit_1,circuit_2]
    return circuit_1
    #for i in S:

# Lista de combinaciones de valores booleanos
values = [1, 0]

# Iterar sobre todas las combinaciones de val1, val2, y val3
for val1 in values:
    for val2 in values:
        for val3 in values:
            result = system(val1, val2, val3)
            print(f'CIRCUIT 1: ({val1} OR {val2}) AND (NOT({val3})) = {result}')
