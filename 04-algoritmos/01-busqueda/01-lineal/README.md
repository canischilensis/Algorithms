# 📜 Explicación Detallada de `linear_search_recursive` y `linear_search`

⬇️⬇️ Abajo de la imagen explicación del Algoritmo ⬇️⬇️

![Busqueda lineal](linear-search.png)

## 📖 Índice

1. [Introducción](#introducción)
2. [Estructura del Código: `linear_search_recursive`](#estructura-del-código-linear_search_recursive)
    - [Definición de la Función](#definición-de-la-función)
    - [Casos en la Función](#casos-en-la-función)
    - [Ejecución y Prueba](#ejecución-y-prueba)
    - [Salida Esperada](#salida-esperada)
3. [Estructura del Código: `linear_search`](#estructura-del-código-linear_search)
    - [Definición de la Función](#definición-de-la-función-1)
    - [Casos en la Función](#casos-en-la-función-1)
    - [Ejecución y Prueba](#ejecución-y-prueba-1)
    - [Salida Esperada](#salida-esperada-1)
4. [Comparación entre Ambos Algoritmos](#comparación-entre-ambos-algoritmos)
5. [Notas Finales](#notas-finales)

---

## Introducción

La búsqueda lineal es un método básico para localizar un elemento dentro de una lista inspeccionando secuencialmente cada posición. Este enfoque es simple pero puede ser menos eficiente para listas grandes. Aquí se analizan dos versiones: una recursiva y otra iterativa.

---

## Estructura del Código: `linear_search_recursive`

### Definición de la Función

```python
def linear_search_recursive(lista, indice, elemento, pasos=0):
```

1. **Parámetros**:  
   - `lista`: La lista en la que se buscará el elemento.  
   - `indice`: La posición actual en la lista que se está inspeccionando.  
   - `elemento`: El valor que se desea buscar.  
   - `pasos`: Cuenta el número de pasos realizados durante la búsqueda (valor inicial = 0).

2. **Propósito**:  
   Busca un elemento recorriendo la lista recursivamente.

---

### Casos en la Función

1. **Depuración con Mensajes DEBUG**  
   ```python
   print(f"DEBUG: 'elemento:'{elemento}' | 'indice:'{indice}' | 'paso:'{pasos}")
   ```
   - Muestra el estado actual de las variables clave (`elemento`, `indice`, `pasos`) en cada llamada recursiva.

2. **Caso Base: Elemento No Encontrado**  
   ```python
   if indice >= len(lista):
       print(f"El elemento {elemento} no se encontró en la lista.")
       return -1
   ```
   - Si el índice supera la longitud de la lista, el elemento no existe en la lista.

3. **Caso Base: Elemento Encontrado**  
   ```python
   if lista[indice] == elemento:
       print(f"El elemento {elemento} se encuentra en la posición {indice}. Se encontró en {pasos} pasos.")
       return indice
   ```

4. **Caso Recursivo**  
   ```python
   elif lista[indice] != elemento:
       return linear_search_recursive(lista, indice + 1, elemento, pasos + 1)
   ```
   - Llama a la función incrementando el índice y el contador de pasos.

---

### Ejecución y Prueba

```python
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 5
    linear_search_recursive(lista, 0, elemento)
```

1. **Lista**: `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]`.  
2. **Elemento a Buscar**: `5`.  
3. **Inicio del Índice**: `0`.

---

### Salida Esperada

```plaintext
DEBUG: 'elemento:'5' | 'indice:'0' | 'paso:'0
DEBUG: 'elemento:'5' | 'indice:'1' | 'paso:'1
DEBUG: 'elemento:'5' | 'indice:'2' | 'paso:'2
El elemento 5 se encuentra en la posición 2. Se encontró en 2 pasos.
```

---

## Estructura del Código: `linear_search`

### Definición de la Función

```python
def linear_search(lista, elemento):
```

1. **Parámetros**:  
   - `lista`: La lista en la que se buscará el elemento.  
   - `elemento`: El valor que se desea buscar.

2. **Propósito**:  
   Localiza un elemento recorriendo secuencialmente la lista mediante un bucle `while`.

---

### Casos en la Función

1. **Variables Iniciales**  
   ```python
   posicion = 0
   pasos = 0
   ```
   - `posicion`: Índice actual en la lista.  
   - `pasos`: Contador de iteraciones.

2. **Depuración con Mensajes DEBUG**  
   ```python
   print(f"DEBUG: 'elemento:{elemento}' | 'posicion:{posicion}' | 'pasos:{pasos}'")
   ```

3. **Elemento Encontrado**  
   ```python
   if lista[posicion] == elemento:
       print(f"Se ha encontrado el {elemento} en la posición {posicion}, en {pasos} pasos")
   ```

4. **Elemento No Encontrado**  
   ```python
   elif posicion == len(lista):
       print(f"El elemento {elemento} no fue encontrado en la lista")
   ```

5. **Actualizar Índice**  
   ```python
   posicion += 1
   ```

---

### Ejecución y Prueba

```python
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 5
    linear_search(lista, elemento)
```

1. **Lista**: `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]`.  
2. **Elemento a Buscar**: `5`.

---

### Salida Esperada

```plaintext
DEBUG: 'elemento:5' | 'posicion:0' | 'pasos:1'
DEBUG: 'elemento:5' | 'posicion:1' | 'pasos:2'
DEBUG: 'elemento:5' | 'posicion:2' | 'pasos:3'
Se ha encontrado el 5 en la posición 2, en 3 pasos
```

---

## Comparación entre Ambos Algoritmos

| Aspecto                     | `linear_search_recursive`             | `linear_search`            |
|-----------------------------|----------------------------------------|----------------------------|
| **Enfoque**                | Recursivo                             | Iterativo (bucle `while`)  |
| **Complejidad Espacial**   | Mayor (llamadas recursivas anidadas)   | Menor                      |
| **Legibilidad**            | Más expresivo                         | Más directo                |
| **Complejidad Temporal**   | \( O(n) \)                            | \( O(n) \)                 |

---

## Notas Finales

1. **Complejidad Temporal**: Ambos algoritmos tienen una complejidad de \( O(n) \), donde \( n \) es el tamaño de la lista.  
2. **Uso Recomendado**:  
   - `linear_search_recursive`: Ideal para aprender y enseñar recursión.  
   - `linear_search`: Más eficiente en términos de uso de memoria para listas grandes.