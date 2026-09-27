lista=[]
def calcular_media():
    media=sum(lista)/len(lista)
    return print(f'La media es: {media}')
def calcular_moda():
    moda=max(set(lista), key=lista.count)
    return print(f'La moda es: {moda}')
def ingreso_numero():
        try:
            n=input("¿Cuántos números deseas ingresar?: ")
        except ValueError:
            print('Debe ingresar un número entero.')
            ingreso_numero()
        try:
            n=int(n)
            for i in range(n):
                try:
                    number = int(input(f'Introduce el número {i+1}: '))
                    lista.append(number)
                except ValueError: 
                    print('Debe ingresar un número entero.')
                    ingreso_numero()
        except ValueError:
            print('Debe ingresar un número entero.')
            ingreso_numero()

if __name__ == '__main__':
    ingreso_numero()
    calcular_media()
    calcular_moda()