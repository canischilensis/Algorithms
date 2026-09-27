#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

# def invertir(cadena):
#     if len(cadena)==0:
#         return cadena
#     else:
#         return invertir(cadena[1:]) + cadena[0]

# if __name__ == "__main__":
#     cadena=str(input("Ingrese una cadena: "))
#     print(invertir(cadena))

#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir(cadena):
    if len(cadena)==0:
        return cadena
    else:
        return invertir(cadena[1:]) + cadena[0]

if __name__ == "__main__":
    #cadena=str(input("Ingrese una cadena: "))
    #print(invertir(cadena))
    assert invertir("malayalam")=="malayalam"
    assert invertir("python")=="nohtyp"
    assert invertir("123456789")=="987654321"
    assert invertir("sometemos")=="sometemos"
    assert invertir("kayak")=="kayak"
    assert invertir("acurruca")=="acurruca"