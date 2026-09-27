grade=float(input("Enter your grade: "))
if 0<=grade and 4.0>grade:
    print("Your grade is: No aprobado.")
elif 4.0<=grade and grade<5.5:
    print("Your grade is: Aprobado.")
elif 5.5<=grade and grade<6.5:
    print("Your grade is: Notable.")
elif 6.5<=grade and grade<7.0:
    print("Your grade is: Sobresaliente.")
elif grade==7.0:
    print("Your grade is: Con honores.")