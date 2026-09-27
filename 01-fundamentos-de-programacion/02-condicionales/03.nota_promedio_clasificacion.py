
grade1 = float(input("Ingrese su primera nota: "))
grade2 = float(input("Ingrese su segunda nota: "))

if grade1<2.2 and grade2<2.2:
    print("Calificacion: Reprobado.No debe rendir la tercera prueba.")
elif grade1>6.4 and grade2>6.4:
    print("Calificacion: Aprobado. No debe rendir la tercera prueba.")
else: 
    print("Debe rendir la tercera prueba.")
    grade3 = float(input("Ingrese su tercera nota: "))
    average_grade = round((grade1 + grade2 + grade3)/3,1)
    if average_grade<=2.8:
        print("Su promedio es:", average_grade, ". Calificacion: Reprobado.")
    elif 7<=average_grade and average_grade>=5.2:
        print("Su promedio es:", average_grade, ". Calificacion: Aprobado.")
    else:
        print("Su promedio es:", average_grade, ". Debe rendir examen para aprobar.")
        exam=float(input("Igrese la nota de su examen: "))
        if exam>=4.0:
            print("Calificacion: Aprobado.")
        else:
            print("Calificacion: Reprobado.")