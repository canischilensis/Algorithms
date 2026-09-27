grade1=float(input("Enter the first grade: "))
grade2=float(input("Enter the second grade: "))
grade3=float(input("Enter the third grade: "))
average_grade=round((grade1+grade2+grade3)/3,1)

if average_grade>=90 and average_grade<=100:
    print("Your average grade is", average_grade, ". You got an A.")
elif average_grade>=80 and average_grade<90:
    print("Your average grade is", average_grade, ". You got a B.")
elif average_grade>=70 and average_grade<80:
    print("Your average grade is", average_grade, ". You got a C.")
elif average_grade>=60 and average_grade<70:
    print("Your average grade is", average_grade, ". You got a D.")
elif average_grade<60:
    print("Your average grade is", average_grade, ". You got an E.")
else:
    print("Error: Invalid grade entered.")