#captura de datos
width_door=round(float(input("Ingrese el ancho de la puerta la cual esta midiendo: ")),2)
height_door=round(float(input("Ingrese el ancho de la puerta la cual esta midiendo: ")),2)
width_wall1 = round(float(input("Ingrese el ancho de la primera pared (en metros): ")),2) 
height_wall1 = round(float(input("Ingrese el alto de la primera pared (en metros): ")),2)
width_wall2 = round(float(input("Ingrese el ancho de la segunda pared (en metros): ")),2)
height_wall2 = round(float(input("Ingrese el alto de la segunda pared (en metros): ")),2)
width_wall3 = round(float(input("Ingrese el ancho de la tercera pared (en metros): ")),2)
height_wall3 = round(float(input("Ingrese el alto de la tercera pared (en metros): ")),2)
width_wall4 = round(float(input("Ingrese el ancho de la cuarta pared (en metros): ")),2)
height_wall4 = round(float(input("Ingrese el alto de la cuarta pared (en metros): ")),2)

#procesamiento
area_wall1=width_wall1*height_wall1
area_wall2=width_wall2*height_wall2
area_wall3=width_wall3*height_wall3
area_wall4=width_wall4*height_wall4
area_door=width_door*height_door

total_are_room=area_wall1+area_wall2+area_wall3+area_wall4
paint=round((total_are_room-area_door)/3,2)

output=print("la cantidad de litros de pintura es de: " + str(paint) + " litros")
#exposción de resultados
