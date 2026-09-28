"""
ETAPA 0 - El punto de partida procedural, y por que se rompe.

Modelo: senalizacion por insulina.
  - proteina  -> la molecula senal (insulina, EGF, FasL). Es una proteina.
  - receptor  -> la proteina receptora anclada en la membrana. Aqui solo
                 existe como una etiqueta de texto, y eso es parte del problema.

Este archivo NO es codigo bueno. Es el codigo que uno escribe con funciones y
diccionarios, llevado hasta el punto donde duele. Cada fallo esta aislado en su
propia funcion para que puedas ejecutarlo y verlo fallar.

Ejecutar con:  python3 etapa0_fallos.py
"""


# =============================================================================
#  PASO 1 - Variables sueltas: una molecula, dos nombres sin relacion entre si
# =============================================================================

nombre_proteina = "insulina"
concentracion_proteina = 5.0

# Para una segunda molecula ya hacen falta dos variables mas, y la unica cosa
# que las relaciona con las de arriba es el sufijo "_2" y tu memoria.
nombre_proteina_2 = "EGF"
concentracion_proteina_2 = 1.2


# =============================================================================
#  PASO 2 - Diccionarios: agrupar los datos de cada molecula en un solo lugar
# =============================================================================

def nueva_proteina(nombre, concentracion):
    """Fabrica un diccionario que representa una molecula senal."""
    return {"nombre": nombre, "concentracion": concentracion}


def nueva_celula(nombre, receptores):
    """Fabrica un diccionario que representa una celula.

    OJO: 'receptores' guarda solo TEXTO, el nombre de la proteina que ese
    receptor reconoceria. No hay una proteina receptora de verdad ahi dentro.
    """
    return {
        "nombre": nombre,
        "glucosa": 0.0,
        "viva": True,
        "receptores": list(receptores),
    }


# =============================================================================
#  PASO 3 - El comportamiento, como funcion suelta y separada de los datos
# =============================================================================

KD_INSULINA = 2.0   # constante de disociacion, nM


def responder_a_insulina(celula, proteina):
    """Calcula la ocupacion del receptor y aumenta la glucosa interna.

    Esta funcion vive FUERA de la celula. Nada la obliga a comprobar si la
    celula que le pasan puede realmente responder a la insulina.
    """
    c = proteina["concentracion"]
    ocupacion = c / (KD_INSULINA + c)     # isoterma de Langmuir
    captado = 50 * ocupacion
    celula["glucosa"] += captado
    return captado, ocupacion


def demo_caso_correcto():
    print("=== Caso correcto (todo funciona) ===")
    hepatocito = nueva_celula("hepatocito", ["insulina"])
    insulina = nueva_proteina("insulina", 5.0)

    captado, ocupacion = responder_a_insulina(hepatocito, insulina)
    print(f"  ocupacion = {ocupacion:.2%}")
    print(f"  captado   = {captado:.1f}")
    print(f"  glucosa   = {hepatocito['glucosa']:.1f}")
    print("  -> Correcto. El problema aparece en cuanto salimos del carril feliz.\n")


# =============================================================================
#  FALLO 1 - NADA PROTEGE LO IMPOSIBLE
#  Un diccionario guarda datos, pero no guarda reglas sobre esos datos.
#  Una concentracion negativa no existe en el universo. El dict la acepta.
#  Lo que falta: ENCAPSULACION (un guardian que valide antes de asignar).
# =============================================================================

def demo_fallo_1():
    print("=== FALLO 1 - Nada protege lo imposible ===")
    hepatocito = nueva_celula("hepatocito", ["insulina"])
    insulina = nueva_proteina("insulina", 5.0)

    # Asignacion imposible. Python no protesta: el error queda latente.
    insulina["concentracion"] = -1.0
    captado, ocupacion = responder_a_insulina(hepatocito, insulina)
    print(f"  con concentracion -1.0 -> ocupacion {ocupacion:.2%}, captado {captado:.1f}")
    print("     la celula EXPULSO glucosa en vez de captarla")

    insulina["concentracion"] = -8.0
    captado, ocupacion = responder_a_insulina(hepatocito, insulina)
    print(f"  con concentracion -8.0 -> ocupacion {ocupacion:.2%}, captado {captado:.1f}")
    print("     ocupacion mayor al 100%: mas receptores ocupados que existentes")

    print(f"  glucosa final = {hepatocito['glucosa']:.1f}  (contaminada, sin ningun error)")
    print("  -> El fallo no se detecto donde se cometio, sino que se propago.\n")


# =============================================================================
#  FALLO 2 - EL COMPORTAMIENTO NO SABE A QUIEN SE APLICA
#  La funcion vive fuera de la celula y nunca mira su lista de receptores.
#  En biologia, la capacidad de responder es una propiedad DE LA CELULA.
#  Aqui es una propiedad de una funcion que anda suelta.
#  Lo que falta: METODO (meter la funcion dentro del dato).
# =============================================================================

def demo_fallo_2():
    print("=== FALLO 2 - El comportamiento no sabe a quien se aplica ===")
    eritrocito = nueva_celula("eritrocito", [])   # sin receptor de insulina
    insulina = nueva_proteina("insulina", 5.0)

    print(f"  receptores del eritrocito: {eritrocito['receptores']}")
    captado, _ = responder_a_insulina(eritrocito, insulina)
    print(f"  captado = {captado:.1f}, glucosa = {eritrocito['glucosa']:.1f}")
    print("  -> Respondio a una senal para la que no tiene receptor.")
    print("     El dato y su comportamiento estan divorciados.\n")


# =============================================================================
#  FALLO 3 - EL DICCIONARIO ACEPTA CUALQUIER CLAVE
#  Un diccionario no tiene forma fija. Cualquiera le anade o le quita campos.
#  Un tipo celular sin identidad estable no es un tipo celular.
#  Lo que falta: CLASE (un molde con forma fija).
# =============================================================================

def demo_fallo_3():
    print("=== FALLO 3 - El diccionario acepta cualquier clave ===")
    hepatocito = nueva_celula("hepatocito", ["insulina"])

    hepatocito["glucossa"] = 100          # typo: Python crea una clave nueva
    print(f"  claves ahora: {sorted(hepatocito.keys())}")
    print("     'glucosa' y 'glucossa' conviven; nadie leera nunca la segunda")

    del hepatocito["viva"]                # ahora falta un campo esencial
    try:
        estado = "viva" if hepatocito["viva"] else "muerta"
    except KeyError as e:
        print(f"  al leer el estado -> KeyError: {e}")
    print("  -> Ni la creacion ni el borrado de campos estan controlados.\n")


# =============================================================================
#  FALLO 4 - CADA MOLECULA NUEVA OBLIGA A EDITAR CODIGO VIEJO
#  La cadena de if/elif crece para siempre. Anadir FasL implica MODIFICAR una
#  funcion ya probada, arriesgando romper los casos anteriores.
#  Lo que falta: POLIMORFISMO (que cada molecula sepa responder por si misma).
# =============================================================================

def responder(celula, proteina):
    """Version 'general'. Nota como la logica de tres tejidos distintos queda
    apelotonada en un mismo bloque, y como cada 'elif' es una cicatriz."""
    nombre = proteina["nombre"]
    c = proteina["concentracion"]

    if nombre == "insulina":
        ocupacion = c / (2.0 + c)
        if ocupacion >= 0.5:
            celula["glucosa"] += 50 * ocupacion
            return f"{celula['nombre']}: GLUT4 a membrana"

    elif nombre == "EGF":
        ocupacion = c / (1.0 + c)
        if ocupacion >= 0.4:
            celula["ciclo"] = celula.get("ciclo", 0) + 1   # .get() para no explotar
            return f"{celula['nombre']}: MAPK activa, entra en ciclo"

    elif nombre == "FasL":
        ocupacion = c / (0.5 + c)
        if ocupacion >= 0.3:
            celula["viva"] = False
            return f"{celula['nombre']}: caspasas, apoptosis"

    # Y aqui iria el proximo elif. Y el siguiente. Para siempre.
    return f"{celula['nombre']}: sin respuesta"


def demo_fallo_4():
    print("=== FALLO 4 - Cada molecula nueva obliga a editar codigo viejo ===")
    celula = nueva_celula("epitelial", ["insulina", "EGF", "FasL"])

    for proteina in (nueva_proteina("insulina", 5.0),
                     nueva_proteina("EGF", 5.0),
                     nueva_proteina("cortisol", 20.0),   # molecula no contemplada
                     nueva_proteina("FasL", 2.0)):
        print(f"  {proteina['nombre']:>9} -> {responder(celula, proteina)}")

    print("  -> 'cortisol' no produce error: produce SILENCIO, que es peor.")
    print("     Para soportarlo hay que abrir y modificar responder().\n")


# =============================================================================
#  FALLO 5 (extra) - NO HAY IDENTIDAD DE TIPO
#  Para Python, una celula y una proteina son exactamente la misma cosa: dict.
#  No puedes preguntar "que eres", ni escribir codigo que dependa de ello, ni
#  detectar que alguien invirtio los argumentos hasta que revienta lejos.
#  Lo que falta: CLASE otra vez, esta vez como identidad, no como forma.
# =============================================================================

def demo_fallo_5():
    print("=== FALLO 5 (extra) - No hay identidad de tipo ===")
    hepatocito = nueva_celula("hepatocito", ["insulina"])
    insulina = nueva_proteina("insulina", 5.0)

    print(f"  type(hepatocito) = {type(hepatocito).__name__}")
    print(f"  type(insulina)   = {type(insulina).__name__}")
    print("     Python no distingue una celula de una proteina.")

    try:
        # Argumentos invertidos. El error no salta en esta linea, sino DENTRO
        # de la funcion, a varios saltos de distancia de la verdadera causa.
        responder_a_insulina(insulina, hepatocito)
    except KeyError as e:
        print(f"  argumentos invertidos -> KeyError: {e}  (lanzado dentro de la funcion)")
    print("  -> El error se manifiesta lejos de donde se cometio.\n")


# =============================================================================
#  RESUMEN - que pide cada fallo
# =============================================================================

RESUMEN = """
| Fallo                          | Lo que falta                       | Se llama       |
|--------------------------------|------------------------------------|----------------|
| 1 Concentracion imposible      | Validar antes de asignar           | Encapsulacion  |
| 2 Comportamiento suelto        | Meter la funcion dentro del dato   | Metodo         |
| 3 Claves arbitrarias           | Un molde con forma fija            | Clase          |
| 4 Cadena de if/elif            | Que cada objeto responda por si    | Polimorfismo   |
| 5 Sin identidad de tipo        | Un tipo propio, no dict            | Clase          |
"""


if __name__ == "__main__":
    demo_caso_correcto()
    demo_fallo_1()
    demo_fallo_2()
    demo_fallo_3()
    demo_fallo_4()
    demo_fallo_5()
    print(RESUMEN)
