"""
1. Validación del ingreso:
Se solicita al usuario que ingrese su ingreso en pesos y se valida que sea un número entero positivo.

2. Validación del número de hijos:
Se solicita al usuario que ingrese el número de hijos y se valida que sea un número entero no negativo.

3. Validación de los años de pertenencia al banco:
Se solicita al usuario que ingrese los años de pertenencia al banco y se valida que sea un número entero no negativo.

4. Validación del estado civil:
Se solicita al usuario que ingrese su estado civil y se valida que sea 'S' (soltero) o 'C' (casado).

5. Validación de la zona de residencia:
Se solicita al usuario que ingrese su zona de residencia y se valida que sea 'R' (rural) o 'U' (urbano).

6. Evaluación de reglas para aprobación de crédito:
Se evalúan las diferentes reglas para decidir si se aprueba o rechaza el crédito, imprimiendo el resultado correspondiente.
"""
# Solicitar y validar ingreso en pesos
while True:
    try:
        income = int(input('Indique su ingreso en pesos: '))
        if income > 0:
            print('Ingreso aceptado')
            break    
        else:
            print('Por favor ingrese un número positivo para su ingreso')
    except ValueError:
        print('Por favor ingrese un número entero para su ingreso')

# Solicitar y validar número de hijos
while True:
    try:
        children = int(input('Indique el número de hijos: '))
        if children >= 0:
            print('Número de hijos aceptado')
            break
        else:
            print('Por favor ingrese un número entero para el número de hijos')
    except ValueError:
        print('Por favor ingrese un número entero para el número de hijos')

# Solicitar y validar años de pertenencia al banco
while True:
    try:
        ranking = int(input('Indique los años de pertenencia al banco: '))
        if ranking >= 0:
            print('Ranking de pertenencia aceptado')
            break
        else:
            print('Por favor ingrese un número entero para los años de pertenencia al banco')
    except ValueError:
        print('Por favor ingrese un número entero para los años de pertenencia al banco')

# Solicitar y validar estado civil
while True:
    maritial_status = str(input('Indique su estado civil (S: soltero, C: casado): ')).upper()
    if maritial_status in ['S', 'C']:
        print('Estado civil aceptado')
        break
    else:
        print('Opción inválida. Por favor ingrese su estado civil válido (S: soltero, C: casado)')

# Solicitar y validar zona de residencia
while True:
    live = str(input('Indique su zona de residencia (R: rural, U: urbano): ')).upper()
    if live in ['R', 'U']:
        print('Zona de residencia aceptada')
        break
    else:
        print('Por favor ingrese una zona de residencia válida (R: rural, U: urbano)')

# El banco usará las siguientes reglas: si se cumple una de ellas, se aprobará el crédito
# Si el cliente ha pertenecido por más de 10 años al banco y tiene dos o más hijos.
if ranking > 10 and children >= 2:
    print('CREDITO APROBADO')
# Si el cliente es casado y tiene más de tres hijos.
elif maritial_status == 'C' and children > 3:
    print('CREDITO APROBADO')
# Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif income > 2500000 and maritial_status == 'S' and live == 'U':
    print('CREDITO APROBADO')
# Si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años.
elif income > 3500000 and ranking > 5:
    print('CREDITO APROBADO')
# Si el cliente vive en una zona rural, es casado y tiene menos de dos hijos.
elif live == 'R' and maritial_status == 'C' and children < 2:
    print('CREDITO APROBADO')
# Si no se cumple ninguna de las reglas anteriores, se rechaza el crédito.
else:
    print('CREDITO RECHAZADO')
