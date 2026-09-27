lista=[]
def menu():
    while True:
        print('''
1. Agregar calificación
2. Mostrar calificaciones
3. Calcular promedio
4. Mejor calificación
5. Salir
''')
        option = int(input('Selecciona una opción: '))
        try:
            if option == 1:
                try:
                    calificacion = float(input('Ingrese una calificación: '))
                    agregar_calificacion(lista, calificacion)
                except ValueError:
                    print('Debe ingresar un número valido.')
                    calificacion = float(input('Ingrese una calificación: '))
                    agregar_calificacion(lista, calificacion)
            elif option == 2:
                mostrar_calificacion(lista)
            elif option == 3:
                calcular_promedio(lista)
            elif option == 4:
                obtener_mejor_calificacion(lista)
            elif option == 6:
                print('Saliendo del programa')
                break
        except ValueError:
            print('Debe ingresar un número entero.')
            menu(lista,option)

def agregar_calificacion(lista,calificacion): 
    lista.append(calificacion)
    return True

def mostrar_calificacion(lista): 
    return print(lista)

def calcular_promedio(lista):
    if not lista:
        print('No hay calificaciones.')
        return 0
    else:
        return print('El promedio es:', sum(lista) / len(lista)) 
def obtener_mejor_calificacion(lista): 
    return print(max(lista))

if __name__ == '__main__':
    menu() 