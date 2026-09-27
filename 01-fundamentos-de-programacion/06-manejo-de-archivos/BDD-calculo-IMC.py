import os
# Necesario para comprobar y eliminar archivos

'''
Resumen del Programa:

Este programa permite gestionar y analizar los Índices de Masa Corporal (IMC) de varias personas.
Las funcionalidades incluyen:

1. Capturar estaturas, pesos y nombres de personas, calcular su IMC y guardar los datos.
2. Mostrar un listado de personas cuyo IMC está por encima del promedio.
3. Mostrar el IMC máximo y mínimo registrado.
4. Mostrar la cantidad de personas en diferentes categorías de peso: bajo peso, peso normal, sobrepeso y obesidad.
5. Guardar los registros de los pacientes en un archivo de texto (.txt).
6. Cargar los datos de estaturas y pesos desde el archivo de texto.
7. Borrar los datos almacenados en el archivo de texto.
8. Mostrar los datos cargados desde el archivo.
9. Proporcionar un menú interactivo para que el usuario seleccione las acciones deseadas.

Cada función del programa está comentada detalladamente para explicar su propósito y funcionamiento.
'''

# 1. Capturar las estaturas, pesos, y otros datos de las personas.
def capture_data(num_people):
    people = load_data_from_file()  # Cargar los datos previos si existen
    for i in range(num_people):
        try:
            name = input(f'Ingrese el nombre de la persona {i + 1}: ')  # Capturar el nombre
            
            weight = float(input(f'Ingrese el peso de {name} en kg: '))  # Capturar el peso
            if not (0 <= weight <= 300):  # Validar que el peso esté en un rango razonable
                raise ValueError('Peso debe estar entre 0 y 300 kg.')
            
            height = float(input(f'Ingrese la estatura de {name} en metros: '))  # Capturar la estatura
            if not (0.5 <= height <= 2.5):  # Validar que la estatura esté en un rango razonable
                raise ValueError('Altura debe estar entre 0.5 y 2.5 metros.')

            imc = round(weight / (height ** 2), 2)  # Calcular el IMC y redondear a 2 decimales
            
            # Crear un diccionario con los datos de la persona
            person = {
                'name': name,
                'weight': weight,
                'height': height,
                'imc': imc
            }
            people.append(person)  # Agregar la persona a la lista

        except ValueError as e:  # Manejar posibles errores en la entrada de datos
            print(f'Error: {e}. Por favor, ingrese los datos nuevamente.')
    
    save_data_to_file(people)  # Guardar los datos al finalizar la captura
    return people  # Devolver la lista de personas actualizada

# 2. Mostrar el listado con aquellos IMC sobre el valor promedio.
def show_overweight_people(people):
    imc_values = [p['imc'] for p in people]  # Extraer los IMC de todas las personas
    if not imc_values:
        print("No hay datos disponibles para calcular el promedio del IMC.")
        return
    mean_imc = sum(imc_values) / len(imc_values)  # Calcular el promedio de los IMC
    print(f'Promedio del IMC: {mean_imc:.2f}')  # Mostrar el promedio del IMC
    print('Listado de personas con IMC sobre el promedio:')
    for person in people:
        if person['imc'] > mean_imc:  # Filtrar personas con IMC superior al promedio
            print(f"{person['name']} - IMC: {person['imc']}")  # Mostrar los detalles de esas personas

# 3. Mostrar el IMC máximo y mínimo registrado.
def show_max_min_imc(people):
    imc_values = [p['imc'] for p in people]  # Extraer los IMC
    if not imc_values:
        print("No hay datos disponibles para determinar el IMC máximo y mínimo.")
        return
    max_imc = max(imc_values)  # Obtener el IMC máximo
    min_imc = min(imc_values)  # Obtener el IMC mínimo
    print(f'Máximo IMC registrado: {max_imc}')  # Mostrar el IMC máximo
    print(f'Mínimo IMC registrado: {min_imc}')  # Mostrar el IMC mínimo

# 4. Mostrar la cantidad de personas con bajo peso, peso normal, sobre peso y obesidad.
def show_weight_categories(people):
    underweight_count = sum(1 for p in people if p['imc'] < 18.5)  # Contar personas con bajo peso
    normal_weight_count = sum(1 for p in people if 18.5 <= p['imc'] < 24.9)  # Contar personas con peso normal
    overweight_count = sum(1 for p in people if 25 <= p['imc'] < 29.9)  # Contar personas con sobrepeso
    obesity_count = sum(1 for p in people if p['imc'] >= 30)  # Contar personas con obesidad

    # Mostrar la cantidad de personas en cada categoría de peso
    print(f'Cantidad de personas con bajo peso: {underweight_count}')
    print(f'Cantidad de personas con peso normal: {normal_weight_count}')
    print(f'Cantidad de personas con sobrepeso: {overweight_count}')
    print(f'Cantidad de personas con obesidad: {obesity_count}')

# 5. Guardar los registros de los pacientes en un archivo .txt.
def save_data_to_file(people, filename="registros_pacientes.txt"):
    try:
        with open(filename, 'w') as file:  # Abrir el archivo en modo escritura
            for person in people:
                # Escribir los datos de cada persona en el archivo, separados por comas
                file.write(f"{person['name']},{person['weight']},{person['height']}\n")
        print(f"Los datos han sido guardados en el archivo {filename}")  # Confirmar la acción
    except IOError as e:
        print(f"Error al guardar los datos en el archivo: {e}")

# 6. Cargar los datos de estaturas y pesos desde el archivo .txt.
def load_data_from_file(filename="registros_pacientes.txt"):
    people = []  # Lista para almacenar los datos
    if os.path.exists(filename):  # Verificar si el archivo existe
        try:
            with open(filename, 'r') as file:  # Abrir el archivo en modo lectura
                for line in file:
                    # Dividir la línea en nombre, peso y estatura
                    parts = line.strip().split(',')
                    if len(parts) != 3:
                        print(f"Línea malformada en el archivo: {line.strip()}")
                        continue  # Saltar líneas malformadas
                    name, weight, height = parts
                    try:
                        weight = float(weight)
                        height = float(height)
                        if height <= 0:
                            print(f"Estatura inválida para {name}.")
                            continue
                        imc = round(weight / (height ** 2), 2)  # Calcular el IMC nuevamente
                        # Agregar la persona a la lista
                        people.append({
                            'name': name,
                            'weight': weight,
                            'height': height,
                            'imc': imc
                        })
                    except ValueError:
                        print(f"Datos numéricos inválidos para {name}.")
            print(f"Datos cargados desde {filename}")  # Confirmar la acción
        except IOError as e:
            print(f"Error al leer el archivo: {e}")
    else:
        print(f"No se encontró el archivo {filename}. Iniciando con una lista vacía.")
    return people  # Devolver la lista de personas cargadas

# 7. Borrar los datos del archivo .txt.
def delete_data_file(filename="registros_pacientes.txt"):
    if os.path.exists(filename):  # Verificar si el archivo existe
        try:
            os.remove(filename)  # Eliminar el archivo
            print(f"El archivo {filename} ha sido borrado.")  # Confirmar la acción
        except OSError as e:
            print(f"Error al borrar el archivo: {e}")
    else:
        print(f"No se encontró el archivo {filename}.")  # Mensaje si el archivo no existe

# 8. Mostrar los datos cargados desde el archivo.
def show_loaded_data(people):
    if people:  # Verificar si hay datos en la lista
        print("Datos cargados:")
        for person in people:
            # Mostrar los datos de cada persona
            print(f"Nombre: {person['name']}, Peso: {person['weight']} kg, Estatura: {person['height']} m, IMC: {person['imc']}")
    else:
        print("No hay datos cargados para mostrar.")  # Mensaje si no hay datos

# Menú principal
def menu():
    people = load_data_from_file()  # Cargar datos respaldados al inicio
    while True:  # Ciclo infinito hasta que el usuario elija salir
        print('''
CONTROL DE ÍNDICES DE MASA CORPORAL
          
---------------------------------------------------------------------------------------------- 

Seleccione su opción introduciendo el número de su opción: 

1. Capturar las estaturas y los pesos de las personas.
2. Mostrar el listado con aquellos IMC sobre el valor promedio.
3. Mostrar el IMC máximo y mínimo registrado.
4. Mostrar la cantidad de personas con bajo peso, peso normal, sobre peso y obesidad.
5. Guardar los registros en un archivo.
6. Borrar los datos del archivo.
7. Mostrar los datos cargados desde el archivo.
8. Salir del programa.
''')
        try:
            option = int(input('Ingrese el número de su opción: '))  # Capturar la opción del menú
            if option == 1:
                num_people = int(input("¿Cuántas personas desea registrar? "))  # Preguntar cuántas personas registrar
                if num_people <= 0:
                    print("Debe registrar al menos una persona.")
                    continue
                people = capture_data(num_people)  # Capturar datos
                save_data_to_file(people)  # Hacer respaldo al terminar de capturar datos
            elif option == 2:
                if people:
                    show_overweight_people(people)  # Mostrar personas con IMC superior al promedio
                else:
                    print("No hay datos disponibles. Por favor, capture datos primero.")
            elif option == 3:
                if people:
                    show_max_min_imc(people)  # Mostrar el IMC máximo y mínimo
                else:
                    print("No hay datos disponibles. Por favor, capture datos primero.")
            elif option == 4:
                if people:
                    show_weight_categories(people)  # Mostrar categorías de peso
                else:
                    print("No hay datos disponibles. Por favor, capture datos primero.")
            elif option == 5:
                if people:
                    save_data_to_file(people)  # Guardar datos en archivo
                else:
                    print("No hay datos disponibles para guardar.")
            elif option == 6:
                delete_data_file()  # Borrar los datos del archivo
                people = []  # Vaciar la lista de personas en memoria
            elif option == 7:
                show_loaded_data(people)  # Mostrar los datos cargados desde el archivo
            elif option == 8:
                print('Saliendo del programa.')  # Mensaje de salida
                break  # Romper el ciclo para salir
            else:
                print('Opción inválida o no se han capturado datos aún. Intente nuevamente.')
        except ValueError:  # Manejar errores si el usuario no ingresa un número
            print('Por favor, ingrese un número entero para la opción.')

if __name__ == "__main__":
    menu()  # Iniciar el programa con el menú principal