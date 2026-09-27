# 📜 Explicación Detallada de `binary_search` y `binary_search_recursive`

⬇️⬇️ Abajo de la imagen explicación del Algoritmo ⬇️⬇️

![Imagen busqeuda binaria](binary-search.png)

## 📖 Índice

1. [Introducción](#introducción)
2. [Estructura del Código: `binary_search`](#estructura-del-código-binary_search)

   * [Definición de la Función](#definición-de-la-función)
   * [Casos en la Función](#casos-en-la-función)
   * [Ejecución y Prueba](#ejecución-y-prueba)
   * [Salida Esperada](#salida-esperada)
3. [Estructura del Código: `binary_search_recursive`](#estructura-del-código-binary_search_recursive)

   * [Definición de la Función](#definición-de-la-función-1)
   * [Casos en la Función](#casos-en-la-función-1)
   * [Ejecución y Prueba](#ejecución-y-prueba-1)
   * [Salida Esperada](#salida-esperada-1)
4. [Comparación entre Ambos Algoritmos](#comparación-entre-ambos-algoritmos)
5. [Notas Finales](#notas-finales)

---

## Introducción

La **búsqueda binaria** es un algoritmo eficiente para localizar un elemento en una lista ordenada. A diferencia de la búsqueda lineal, reduce a la mitad el espacio de búsqueda en cada paso, logrando una complejidad temporal de $O(\log n)$. Aquí se analizan dos versiones del algoritmo: una iterativa (`binary_search`) y otra recursiva (`binary_search_recursive`).

---

## Estructura del Código: `binary_search`

### Definición de la Función

```python
def binary_search(lista, elemento):
```

1. **Parámetros**:

   * `lista`: Lista ordenada donde se realizará la búsqueda.
   * `elemento`: Valor que se desea encontrar.

2. **Propósito**:
   Implementa la búsqueda binaria utilizando un bucle `while`.

---

### Casos en la Función

1. **Variables Iniciales**

   ```python
   der = len(lista) - 1
   izq = 0
   pasos = 0
   encontrado = False
   ```

2. **Depuración con Mensajes DEBUG**

   ```python
   print(f"DEBUG1: 'derecha: {der}' | 'izquierda: {izq}' | pasos: {pasos} | medio: {medio} | elemento: {elemento}")
   ```

3. **Elemento Encontrado**

   ```python
   if lista[medio] == elemento:
       print(f"elemento {elemento} se encuentra en la posicion {medio}, el algoritmo lo ubico en {pasos} pasos")
   ```

4. **Actualizar Límites**

   ```python
   elif lista[medio] > elemento:
       der = medio - 1
   elif lista[medio] < elemento:
       izq = medio + 1
   ```

5. **Elemento No Encontrado**

   ```python
   if encontrado == False:
       print(f"el elemento {elemento} no esta en la lista")
   ```

---

### Ejecución y Prueba

```python
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 5
    binary_search(lista, elemento)
```

---

### Salida Esperada

```plaintext
DEBUG1: 'derecha: 11' | 'izquierda: 0' | pasos: 1 | medio: 5 | elemento: 5
DEBUG2: 'el valor de la derecha se cambia a: 4' | ...
DEBUG1: 'derecha: 4' | 'izquierda: 0' | pasos: 2 | medio: 2 | elemento: 5
elemento 5 se encuentra en la posicion 2, el algoritmo lo ubico en 2 pasos
```

---

## Estructura del Código: `binary_search_recursive`

### Definición de la Función

```python
def binary_search_recursive(lista, elemento, left=0, right=None, pasos=0):
```

1. **Parámetros**:

   * `lista`: Lista ordenada.
   * `elemento`: Valor que se desea encontrar.
   * `left`: Índice izquierdo del rango de búsqueda.
   * `right`: Índice derecho (se define en la primera llamada).
   * `pasos`: Contador de pasos en la recursión.

2. **Propósito**:
   Realiza la búsqueda binaria mediante llamadas recursivas.

---

### Casos en la Función

1. **Inicialización de `right`**

   ```python
   if right is None:
       right = len(lista) - 1
   ```

2. **Condición de Continuación**

   ```python
   if left <= right:
   ```

3. **Depuración con Mensajes DEBUG**

   ```python
   print(f"DEBUG: 'derecha: {right}' | 'izquierda: {left}' | pasos: {pasos} | elemento: {elemento}")
   ```

4. **Elemento Encontrado**

   ```python
   if lista[medio] == elemento:
       print(f"elemento {elemento} se encuentra en la posicion {medio}, el algoritmo lo ubico en {pasos} pasos")
   ```

5. **Llamadas Recursivas**

   ```python
   elif lista[medio] > elemento:
       return binary_search_recursive(lista, elemento, left, medio-1, pasos)
   elif lista[medio] < elemento:
       return binary_search_recursive(lista, elemento, medio+1, right, pasos)
   ```

6. **Elemento No Encontrado**

   ```python
   if not encontrado:
       print(f"el elemento {elemento} no esta en la lista")
   ```

---

### Ejecución y Prueba

```python
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 21
    binary_search_recursive(lista, elemento)
```

---

### Salida Esperada

```plaintext
DEBUG: 'derecha: 11' | 'izquierda: 0' | pasos: 1 | elemento: 21
DEBUG2: 'derecha: 11' | el valor de la izquierda se cambia a: 6
DEBUG: 'derecha: 11' | 'izquierda: 6' | pasos: 2 | elemento: 21
DEBUG2: ... izquierda se cambia a: 9
DEBUG: 'derecha: 11' | 'izquierda: 9' | pasos: 3 | elemento: 21
elemento 21 se encuentra en la posicion 10, el algoritmo lo ubico en 3 pasos
```

---

## Comparación entre Ambos Algoritmos

| Aspecto                  | `binary_search`                    | `binary_search_recursive`          |
| ------------------------ | ---------------------------------- | ---------------------------------- |
| **Enfoque**              | Iterativo (bucle `while`)          | Recursivo                          |
| **Complejidad Espacial** | Menor (una sola pila de ejecución) | Mayor (varias llamadas anidadas)   |
| **Legibilidad**          | Más directo                        | Más expresivo para entender lógica |
| **Complejidad Temporal** | $O(\log n)$                        | $O(\log n)$                        |

---

## Notas Finales

1. **Requisitos Previos**: Ambos algoritmos requieren que la lista esté **ordenada**.
2. **Uso Recomendado**:

   * `binary_search`: Más eficiente para entornos con recursos limitados.
   * `binary_search_recursive`: Útil para comprender el concepto de recursión.
3. **Ventajas sobre la Búsqueda Lineal**: En listas grandes, la búsqueda binaria es significativamente más rápida que la búsqueda secuencial.