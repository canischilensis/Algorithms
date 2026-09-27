grade1 = float(input("Ingrese su primera nota: "))
grade2 = float(input("Ingrese su segunda nota: "))
grade3 = float(input("Ingrese su tercera nota: "))

average_grade = round((grade1 + grade2 + grade3)/3,1)

if average_grade>=1 and 4>average_grade:
    print("Su promedio es:", average_grade, ". Calificacion: No aprobado.")
elif 4<=average_grade and average_grade<5.5:
    print("Su promedio es:", average_grade, ". Calificacion: Aprobado.")
elif 5.5<=average_grade and average_grade<6.5:
    print("Su promedio es:", average_grade, ". Calificacion: Notable.")
elif 6.5<=average_grade and average_grade<7.0:
    print("Su promedio es:", average_grade, ". Calificacion: Sobresaliente.")
elif average_grade==7.0:
    print("Su promedio es:", average_grade, ". Calificacion: Con honores.")
else:
    print("Error: Nota invalida.")

