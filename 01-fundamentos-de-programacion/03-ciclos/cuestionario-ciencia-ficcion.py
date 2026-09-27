
""" 
Este código implementa un juego de trivia de ciencia ficción para dos jugadores. Aquí está la descripción de sus funcionalidades:

1. LIBRERIAS

1.1. Bibliotecas Importadas:
    - `random`: Para seleccionar preguntas de manera aleatoria.
1.2. Preguntas:
    - Una variable `questions` que contiene un diccionario de 20 preguntas. Cada pregunta tiene su número, enunciado, alternativas, respuesta correcta y retroalimentación.

2. FASE DE CONFIGURACION 

2.1.Bienvenida:
    - Muestra un mensaje de bienvenida y solicita los nombres de los jugadores, que se almacenan en la lista `players`.

2.2.Instrucciones:
    - Muestra las instrucciones del juego a los jugadores.

2.3.Cantidad de Preguntas:
    - Solicita a los jugadores la cantidad de preguntas que desean responder, con un máximo de 10 por jugador. Maneja errores si el usuario ingresa un valor inválido.

3. FASE DE PREGUNTA-RESPUESTA

3.1.Inicio del Juego:
    - Inicializa los puntajes de ambos jugadores.
    - Baraja las preguntas para asegurarse de que sean seleccionadas aleatoriamente.

3.2.Desarrollo del Juego:
    - Alterna entre los jugadores para responder las preguntas.
    - Muestra la pregunta y las alternativas al jugador actual.
    - Solicita la respuesta del jugador y verifica si es correcta.
    - Actualiza el puntaje del jugador según la respuesta.
    - Muestra retroalimentación en caso de respuesta incorrecta.
    - Muestra los puntajes actuales después de cada turno.

4. FASE DE CIERRE

4.1. Determinación del Ganador:
    - Al finalizar el juego, determina y muestra el ganador según los puntajes acumulados.
    - Muestra el puntaje final de cada jugador.

Este programa proporciona una experiencia interactiva de trivia de ciencia ficción, gestionando turnos, verificando respuestas y manteniendo un puntaje para determinar el ganador.
""" 


#libreria random para escoger la pregutnas de forma azarosa
import random
#variable que tiene un diccionario y tiene las 20 preguntas.
#tiene un diccionario dentro de un diccionario
questions = {
    'question1': {
        'number': 1,
        'question': "¿Quién es considerado el padre de la ciencia ficción?",
        'alternatives': """
        A) Isaac Asimov
        B) Jules Verne
        C) H.G. Wells""",
        'correct': "B",
        'feedback': """Jules Verne es considerado uno de los padres de la ciencia ficción por sus novelas que combinan aventuras y ciencia, como "Viaje al centro de la Tierra" y "Veinte mil leguas de viaje submarino"."""
    },
    'question2': {
        'number': 2,
        'question': "¿Cuál de las siguientes obras es un ejemplo de ciencia ficción dura?",
        'alternatives': """
        A) "Dune" de Frank Herbert
        B) "2001: Una odisea del espacio" de Arthur C. Clarke
        C) "Fahrenheit 451" de Ray Bradbury""",
        'correct': "B",
        'feedback': """'2001: Una odisea del espacio' es un ejemplo de ciencia ficción dura porque se enfoca en la precisión científica y técnica."""
    },
    'question3': {
        'number': 3,
        'question': "¿Qué tema común se aborda en 'Un mundo feliz' de Aldous Huxley?",
        'alternatives': """
        A) Inteligencia artificial
        B) Ingeniería genética
        C) Colonización espacial""",
        'correct': "B",
        'feedback': """'Un mundo feliz' trata sobre una sociedad que utiliza la ingeniería genética para controlar la población y mantener la estabilidad social."""
    },
    'question4': {
        'number': 4,
        'question': "¿En qué novela aparece el concepto de 'Gran Hermano'?",
        'alternatives': """
        A) "1984"
        B) "Fahrenheit 451"
        C) "Brave New World""",
        'correct': "A",
        'feedback': """En '1984' de George Orwell, el Gran Hermano es el líder omnipresente y vigilante de un estado totalitario."""
    },
    'question5': {
        'number': 5,
        'question': "¿Quién es el autor de 'Frankenstein'?",
        'alternatives': """
        A) Mary Shelley
        B) H.G. Wells
        C) Jules Verne""",
        'correct': "A",
        'feedback': """Mary Shelley escribió 'Frankenstein', considerada una de las primeras obras de ciencia ficción."""
    },
    'question6': {
        'number': 6,
        'question': "¿Cuál es el enfoque principal del subgénero cyberpunk?",
        'alternatives': """
        A) Realidades virtuales y tecnologías avanzadas
        B) Robots y androides
        C) Mutaciones genéticas""",
        'correct': "A",
        'feedback': """El cyberpunk se centra en realidades virtuales, ciberespacios y la integración de la tecnología en la sociedad."""
    },
    'question7': {
        'number': 7,
        'question': "¿Qué novela popularizó el concepto de 'tres leyes de la robótica'?",
        'alternatives': """
        A) "Yo, Robot"
        B) "Dune"
        C) "2001: Una odisea del espacio""",
        'correct': "A",
        'feedback': """Isaac Asimov introdujo las tres leyes de la robótica en su colección de cuentos 'Yo, Robot'."""
    },
    'question8': {
        'number': 8,
        'question': "¿Cuál de estas series de televisión es un ejemplo clásico de ciencia ficción?",
        'alternatives': """
        A) "Star Trek"
        B) "Breaking Bad"
        C) "Game of Thrones""",
        'correct': "A",
        'feedback': """'Star Trek' es una serie de televisión icónica en el género de la ciencia ficción, que explora el espacio y el futuro de la humanidad."""
    },
    'question9': {
        'number': 9,
        'question': "¿Qué autor es conocido por su serie de novelas 'Fundación'?",
        'alternatives': """
        A) Isaac Asimov
        B) Robert Heinlein
        C) Arthur C. Clarke""",
        'correct': "A",
        'feedback': """Isaac Asimov es el autor de la serie 'Fundación', que trata sobre el declive y resurgimiento de un imperio galáctico."""
    },
    'question10': {
        'number': 10,
        'question': "¿En qué novela aparece el personaje 'Paul Atreides'?",
        'alternatives': """
        A) "Dune"
        B) "Neuromancer"
        C) "1984""",
        'correct': "A",
        'feedback': """Paul Atreides es el protagonista de 'Dune', una novela de Frank Herbert sobre intrigas políticas y ecología en un planeta desértico."""
    },
    'question11': {
        'number': 11,
        'question': "¿Cuál es el tema central de la novela 'El hombre en el castillo' de Philip K. Dick?",
        'alternatives': """
        A) Realidades alternativas
        B) Viaje en el tiempo
        C) Inteligencia artificial""",
        'correct': "A",
        'feedback': """'El hombre en el castillo' explora una realidad alternativa en la que los Aliados perdieron la Segunda Guerra Mundial."""
    },
    'question12': {
        'number': 12,
        'question': "¿Qué película de ciencia ficción está basada en una obra de Arthur C. Clarke?",
        'alternatives': """
        A) "2001: Una odisea del espacio"
        B) "Blade Runner"
        C) "Minority Report""",
        'correct': "A",
        'feedback': """'2001: Una odisea del espacio' es una película basada en la novela homónima de Arthur C. Clarke, dirigida por Stanley Kubrick."""
    },
    'question13': {
        'number': 13,
        'question': "¿Cuál de estos autores es conocido por escribir ciencia ficción blanda?",
        'alternatives': """
        A) Ursula K. Le Guin
        B) Kim Stanley Robinson
        C) Greg Egan""",
        'correct': "A",
        'feedback': """Ursula K. Le Guin es conocida por su enfoque en aspectos sociológicos y antropológicos, característicos de la ciencia ficción blanda."""
    },
    'question14': {
        'number': 14,
        'question': "¿Qué novela explora una sociedad distópica donde los libros están prohibidos?",
        'alternatives': """
        A) "Fahrenheit 451"
        B) "1984"
        C) "Brave New World""",
        'correct': "A",
        'feedback': """'Fahrenheit 451' de Ray Bradbury trata sobre una sociedad futura donde los bomberos queman libros para suprimir el conocimiento."""
    },
    'question15': {
        'number': 15,
        'question': "¿En qué novela se popularizó la idea de un 'anillo-mundo'?",
        'alternatives': """
        A) "Ringworld" de Larry Niven
        B) "Neuromancer" de William Gibson
        C) "Hyperion" de Dan Simmons""",
        'correct': "A",
        'feedback': """'Ringworld' de Larry Niven presenta un anillo artificial gigantesco que orbita una estrella."""
    },
    'question16': {
        'number': 16,
        'question': "¿Qué autor escribió 'Las estrellas, mi destino'?",
        'alternatives': """
        A) Alfred Bester
        B) Isaac Asimov
        C) Philip K. Dick""",
        'correct': "A",
        'feedback': """Alfred Bester es el autor de 'Las estrellas, mi destino', una novela sobre venganza y teletransportación."""
    },
    'question17': {
        'number': 17,
        'question': "¿Cuál es el nombre del superordenador en '2001: Una odisea del espacio'?",
        'alternatives': """
        A) HAL 9000
        B) GERTY
        C) Skynet""",
        'correct': "A",
        'feedback': """HAL 9000 es el superordenador de '2001: Una odisea del espacio', conocido por su inteligencia avanzada y comportamiento problemático."""
    },
    'question18': {
        'number': 18,
        'question': "¿En qué novela aparece el concepto de la 'nave generacional'?",
        'alternatives': """
        A) "Non-Stop" de Brian Aldiss
        B) "Rendezvous with Rama" de Arthur C. Clarke
        C) "Hyperion" de Dan Simmons""",
        'correct': "A",
        'feedback': """'Non-Stop' de Brian Aldiss trata sobre una nave espacial cuyos habitantes han olvidado su propósito original."""
    },
    'question19': {
        'number': 19,
        'question': "¿Qué tema aborda principalmente 'Solaris' de Stanisław Lem?",
        'alternatives': """
        A) Contacto con una forma de vida alienígena
        B) Exploración espacial
        C) Distopía futurista""",
        'correct': "A",
        'feedback': """'Solaris' se centra en el encuentro con una forma de vida alienígena en un planeta cubierto de un océano viviente."""
    },
    'question20': {
        'number': 20,
        'question': "¿Cuál de estos autores es conocido por su estilo literario poético y filosófico en la ciencia ficción?",
        'alternatives': """
        A) Ursula K. Le Guin
        B) H.G. Wells
        C) Philip K. Dick""",
        'correct': "A",
        'feedback': """Ursula K. Le Guin es conocida por su estilo literario poético y sus profundas exploraciones filosóficas en obras como 'La mano izquierda de la oscuridad'."""
    }
}

#================================================================================================================================================================
#2. FASE DE CONFIGURACION
#BIENVENIDA
#IDENTIFICAR AL USUARIO
#variable 'welcome' para dar la bienvenida a los usuarios
welcome="""
=================================================
BIENVENIDOS AL JUEGO DE TRIVIA DE CIENCIA FICCIÓN
=================================================
\n
Ingrese el nombre de los jugadores
"""
#salida para la bienvenida a los usuarios
print(welcome)
#variable jugadores en una lista que guarda el nombre de los jugadores
players=[]
#ciclo for para ingresar los nombres de jugadores en la varaible 'players'
for i in range(2):
    player = input(f"\nIngrese el nombre del jugador número {i + 1}: ").strip().title()
    players.append(player)
    print(f"Hola {player}, tú eres el jugador número {i + 1}")

#variable instrucciones para entregar informacion a los usuarios. Dentro de esta varaible se llama los datos de la lista 'players' para que los usuarios sientan cercania.
instructions= f"""
=================================================================

INSTRUCCIONES DEL JUEGO:

1. Ingrese la cantidad de preguntas que desean responder por jugador. El máximo es de 10 preguntas por jugador.
2. El juego se desarrolla por turnos. La primera pregunta la responde {players[0]}, quien podrá observar las alternativas.
3. {players[0]}, seleccione la letra de su alternativa correcta.
4. Una vez ingresada la alternativa correcta de {players[0]}, si la respuesta es correcta, aparecerá un mensaje que dirá "Su respuesta es correcta" y sumará un punto.
5. Si la respuesta de {players[0]} es incorrecta, no sumará puntos y recibirá una retroalimentación de la pregunta. Después de la retroalimentación, es el turno de {players[1]}.
6. Ahora es el turno de {players[1]}, quien debe leer la pregunta y seleccionar su alternativa correcta.
7. {players[1]}, seleccione la letra de su alternativa correcta. Si la respuesta es correcta, sumará un punto. Si es incorrecta, recibirá una retroalimentación de la pregunta.
8. El juego continuará por turnos hasta completar la cantidad de preguntas seleccionadas por jugador.
9. Ganará el jugador que tenga mayor puntaje.
\n
"""
#salida de las instrucciones
print(instructions)

#================================================================================================================================================================
#INICIO DEL JUEGO
#CANTIDAD DE PREGUNTAS POR JUGADOR
#variable de entrada para que el usario ingrese un numero de la cantidad de preguntas por jugador
number_of_questions=input("""Ingrese la cantidad de preguntas por persona que quieren responder. Debe ingresar un numero entre 1 y 10: """)
#manejo de errores a partir del tipo de dato que ingresa el usuario
try:
    #convierte el input tipo de dato por defecto en 'str'en un 'int'
    number_of_questions=int(number_of_questions)
    #chequear que el numero de preguntas sea mayor o igual a 1 y menor o igual a 10 o distinto a un tipo de dato 'int' o 'float'
    if number_of_questions>=10:
        #si el usuario ingresa un numero mayor a 10 se entra se activa estas lineas
        number_of_questions = 10
        print("El máximo de preguntas por jugador es 10. Se ajustará a 10 preguntas por jugador.")
        print(f"Cada jugador respondera {number_of_questions} preguntas.\n")
    elif number_of_questions<1:
        #si el usuario ingresa un numero menor a 1 se entra se activa estas lineas
        print("El minimo de preguntas por jugador es 1. Se ajustará a 1 pregunta por jugador.")
        number_of_questions = 1
        print(f"Cada jugador respondera {number_of_questions} pregunta.\n")
    else: 
        #si el jugador ingresa un dato número entre 1 a 10 se activa estas lineas        
        print(f"La cantidad de preguntas que debe responder por jugador es de {number_of_questions} preguntas.")

except ValueError:
    #si el usuario ingresa un dato que no se puede transformar en una tipo dato 'int'.
    #ValueError: es una expcecion estandar y se activa cuando el valor de la varaible 'number_of_questions' es incorrecto.
    #se cambia la variable por un valor azaroso entre 1 a 10 por medio de la funcion .randint() de la libreria random. 
    number_of_questions =random.randint(1,10)
    #informacion para el usuario sobre su error, informa lo que hara el programa y la cnatidad de pregutnas que van a responder por jugador 
    print(f"""
        Debe ingresar un numero entre 1 a 20 preguntas por jugador.
        Se le seleccionara la cantidad de preguntas al azar. 
        La cantidad de preguntas que debe responder por jugador es de {number_of_questions} preguntas. \n""")

#3.FASE PREGUNTA-RESPUESTA
#INICIO DEL JUEGO
#variables de los puntajes de los jugadopres antes de partir
score_player1=0
score_player2=0
#variable lista que convierte cada pregunta 'keys' en una lista
question_keys=list(questions.keys()) 
#Barajar las preguntas con la funcion '.shuffle()' de la libreria random
random.shuffle(question_keys)
#Asegurarse de tener suficientes preguntas para que cada jugador responda preguntas azarosas y que no sea repetidas. 
if len(question_keys) < number_of_questions * 2:
    raise ValueError("No hay suficientes preguntas para el número de turnos.")
#ciclo que se repite hasta la cantidad de preguntas que puso el usuario en el cual deberan presponder cada jugador
#i es la variable del numero de preguntas que han escogido los usuarios para que responda cada jugador
for i in range(number_of_questions):
    #ciclo for que genera los turnos para que jugador responda cada pregunta a partir de la cantidad de preguntas que deberan responder cada jugador
    for j in range(2):
        #un espacio para dar un orden en pantalla
        print("\n================================================================\n")
        #varaible que llama el nombre del jugador a partir de la lista 'players' en funcion del turno declarado por la variable j del ciclo for
        current_player=players[j]
        print(f"""\nEs el turno del jugador {current_player}""")
        
        #SELECCIONAR UNA PREGUNTA PARA EL JUGADOR
        #variable 'question_key' Obtiene y elimina una pregunta de la lista de la cual fue seleccionada de forma azarosa en el primer ciclo, por eso tiene la variable i. Asi las pregutnas por jugador no se repite 
        question_key = question_keys.pop(i)  
        #variable 'activity' toma un keys del diccionario a partir del numero que fue seleccionado al azar por la variable 'question_key'
        activity = questions[question_key]

        #MOSTRAR PREGUNTAS POR JUGADOR
        #variable que informa al usario a responder la pregunta y que llama la pregunta a paritr del valor 'question' del diccionario 
        activity_question=f"\nResponda la siguiente pregunta {activity['question']}\n"
        #variable que informa al usario las alternativas de respuesta para la pregunta y que llama las alternativas a partir del valor 'alternatives' del diccionario
        activity_alternative=f"\nSeleccione su alternativa correcta:\n {activity['alternatives']}"
        #salida de las dos variables
        print(f"\t {activity_question}")
        print(f"\t {activity_alternative}")
        #Obtener respuesta del jugador
        #se ingresa la respuesta. Si el usuario ingresa en minuscula, el dato 'int' cambia de mayuscula por medio de la funcion .upper()
        option=str(input("Ingrese su respuesta, tenga cuidado porque si no se escribe una letra perdera su puntaje del turno. Escriba A, B o C: ")).upper()
        #Verificar respuesta del jugador
        if option==activity['correct']:
            #Si la respuesta del jugador es correcta, se suma un punto al puntaje del jugador y se informa al jugador
            print("\nSu respuesta es correcta. Ha sumado un punto.")
            #si el jugador del turno j es igual al primer jugador de la lista players, perteneciente al primer jugador
            if players[j]==players[0]:
                #se le suma un punto a la variable 'score_player1'
                score_player1=score_player1+1
            #si el jugador del turno j es igual al segundo jugador de la lista players, perteneciente el segundo jugador    
            elif players[j]==players[1]:
                #se le suma un punto a la variable 'score_player2'
                score_player2=score_player2+1     
        elif option!=activity['correct']:
            #Si la respuesta del jugador es incorrecta, se informa al jugador y se le resta un punto al puntaje del jugador.
            #incluso si ingresa cualquier tipo de dato diferente a la respuesta correcta ejecutan estas lineas
            print ("\nSu respuesta es incorrecta. No ha sumado puntaje")
            #esta salida llama al valor 'feedback' a la clave pregunta del diccionario para entregar una retroalimentacion al jugador del porque se equivoco.
            print (f"La respuesta correcta es {activity['correct']} porque {activity['feedback']}")
        # Mostrar puntajes actuales 
        print(f"Puntaje actual de {players[0]}: {score_player1}")
        print(f"Puntaje actual de {players[1]}: {score_player2}")
        #se cierran el ciclo de turnos ahora se devuelve al ciclo for que avanza a la siguiente tanda de pregunta que han elegido el usuario para que responda cada jugador. 

#salida para dar orden y separacion a la interfaz de usuario 
print("\n================================================================\n")
#4. FASE DE CIERRE
#Determinar ganador
if score_player1>score_player2:
    #si el jugador 1 tiene mayor puntaje que el jugador 2, se genera una una salida que el ganador es el jugador 1 
    print(f"El ganador es {players[0]}")
elif score_player1==score_player2:
    #si ambos jugadores tiene los mismos puntaje 
    #se genera una salida que se ha llevado un empate en el juego de preguntas y se informa que el puntaje es igual para ambos jugadores. 
    print("Ha habido un empate")
else: 
    #si el jugador 2 tiene mayor puntaje que el jugador 1, se genera una una salida que el ganador es el jugador 2
    print(f"El ganador es {players[1]}")

#Mostrar puntaje final
print(f"""
    El puntaje final es: 
    Jugador {players[0]} obtuviste {score_player1} puntos.
    Jugador {players[1]} obtuviste {score_player2} puntos.
    """)
print("\n================================================================\n")