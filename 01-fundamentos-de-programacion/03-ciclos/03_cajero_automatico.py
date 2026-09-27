#usuario 10334151
#clave 1803
#tiene un monto de 100000
user1=10334151
pass1=1803
cash1=100000
contador=3
while contador!=0:
    usuario=int(input('Ingrese su usuario: '))
    clave=int(input('Ingrese su clave: '))
    contador=contador-1
    if contador == 0:
        print(f'fUsuario o clave invalido. Solo quedan {contador} intentos. Tarjeta bloqueada.')
    elif usuario!=user1 and clave!=pass1:
        print(f'Usuario o clave invalido. Solo quedan {contador} intentos')
    else:
        print(f'Bienvenido {usuario}')
        while cash1<=100000:
            out=int(input('ingrese el monto que desea retirar:$ '))
            cash1=cash1-out
            if cash1>0:
                try:
                    print(f'Retiro exitoso. Saldo en cuenta corriente: ${cash1}')
                    operation=int(input('Desea realizar otra operacion? (s/n): '))
                    if operation=='s':
                        out=int(input('ingrese el monto que desea retirar: '))
                    elif operation=='n':
                        print(f'Gracias por usar el cajero. Saldo final ${cash1}')
                    else:
                        print(f'Opcion invalida. Gracias por usar el cajero. Saldo final ${cash1}')
                    break
                except ValueError:
                    print('Por favor ingrese un numero entero valido para hacer un retiro')