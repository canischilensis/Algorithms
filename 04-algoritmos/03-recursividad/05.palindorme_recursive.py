def palindromo(palabra):
  if len(palabra)<=1: #si la palabra tiene cero letras o una letra si es un palíndromo
    print("Si es un palindromo")
  else:               #de lo contrario
    if palabra[0]!=palabra[-1]:  #compara la primera y la última letra de la palabra
      print("No es un palindromo") #si son diferentes no es un palíndromo
    else:                          #si son iguales
      palabra=palabra[1:-1]        #elimina la primera y la última letra del string
      palindromo(palabra)          #vuelve a llamar a la función con este string más pequeño

candidato=input('Dime una palabra: ').lower()
palindromo(candidato)
