# Verificación de Diccionario Alienígena

![Texto alternativo](photo-alien.png)

## Descripción del Proyecto

Este repositorio contiene una solución al problema **"Verificación de Diccionario Alienígena"**, habitual en entrevistas de empresas tecnológicas como Facebook, Microsoft y Google. El objetivo es comprobar si una lista de palabras está ordenada según un alfabeto personalizado (alienígena).

## Planteamiento del Problema

* **Entradas**:

  * `words`: lista de cadenas, por ejemplo, `["apple", "app"]`.
  * `order`: cadena de 26 caracteres que define el alfabeto alienígena, p. ej. `"hlabcdefgijkmnopqrstuvwxyz"`.

* **Salida**:

  * Valor booleano (`True` o `False`):

    * `True` si `words` está ordenada lexicográficamente según `order`.
    * `False` en caso contrario.

## Solución en Python

```python
def alien_sorted(words, order):
    # 1) Construir el diccionario que mapea cada letra a su posición
    letter_order = {}
    for idx, letter in enumerate(order):
        letter_order[letter] = idx

    # 2) Función interna para comparar dos palabras según el alfabeto alienígena
    def compare(w1, w2):
        n = min(len(w1), len(w2))
        for j in range(n):
            if letter_order[w1[j]] < letter_order[w2[j]]:
                return True   # w1 < w2
            if letter_order[w1[j]] > letter_order[w2[j]]:
                return False  # w1 > w2
        # Si todas las letras coinciden hasta la longitud más corta:
        return len(w1) <= len(w2)

    # 3) Verificar cada par de palabras consecutivas
    for i in range(1, len(words)):
        if not compare(words[i-1], words[i]):
            return False
    return True
```

### Ejemplo de uso

```python
if __name__ == "__main__":
    palabras = ["hola", "holaa", "holb"]
    orden = "hlabcdefgijkmnopqrstuvwxyz"
    resultado = alien_sorted(palabras, orden)
    print("¿La lista está ordenada?", resultado)  # → True
```

## Análisis de Complejidad

* **Tiempo:** O(n · L)

  * n = número de palabras en la lista.
  * L = longitud máxima de las palabras.
* **Espacio extra:** O(1) (aparte de la entrada y la pila de llamadas).

## Importancia del Ejercicio

* Refuerza conceptos de **comparación lexicográfica** personalizada y uso de diccionarios.
* Evalúa la capacidad de diseñar lógica clara y eficiente con estructuras de datos básicas.
* Frecuente en entrevistas técnicas para medir razonamiento algorítmico.

## Consejos Prácticos

1. Divide el problema en las tres etapas esenciales (mapa, comparación, verificación).
2. Añade comentarios para explicar cada bloque de código.
3. Prueba con casos límite: palabras idénticas, una palabra prefijo de otra, caracteres fuera de orden, etc.
4. Verifica manualmente pequeños ejemplos antes de automatizar pruebas.