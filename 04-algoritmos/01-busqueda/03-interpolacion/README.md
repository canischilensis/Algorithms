# 📜 Explicación Detallada de `interpolation_search` y `interpolation_search_recursive`

⬇️⬇️ Abajo de la imagen explicación del Algoritmo ⬇️⬇️

![Imagen búsqueda por interpolación](interpolation_search.png)

## 📖 Índice

1. [Introducción](#introducción)
2. [Estructura del Código: `interpolation_search`](#estructura-del-código-interpolation_search)

   * [Definición de la Función](#definición-de-la-función)
   * [Casos en la Función](#casos-en-la-función)
   * [Ejecución y Prueba](#ejecución-y-prueba)
   * [Salida Esperada](#salida-esperada)
3. [Estructura del Código: `interpolation_search_recursive`](#estructura-del-código-interpolation_search_recursive)

   * [Definición de la Función](#definición-de-la-función-1)
   * [Casos en la Función](#casos-en-la-función-1)
   * [Ejecución y Prueba](#ejecución-y-prueba-1)
   * [Salida Esperada](#salida-esperada-1)
4. [Comparación entre Ambos Algoritmos](#comparación-entre-ambos-algoritmos)
5. [Notas Finales](#notas-finales)

---

## Introducción

La **búsqueda por interpolación** es una técnica de búsqueda eficiente diseñada para listas ordenadas y distribuidas uniformemente. A diferencia de la búsqueda binaria que busca el punto medio, este algoritmo **estima la posición** del valor buscado usando una fórmula basada en interpolación lineal. Su complejidad es aproximadamente $O(\log\log n)$ en el mejor de los casos y $O(n)$ en el peor caso.

---

## Estructura del Código: `interpolation_search`

### Definición de la Función

```python
def interpolation_search(arr, e):
````

1. **Parámetros**:

   * `arr`: Lista ordenada de elementos.
   * `e`: Elemento que se desea encontrar.

2. **Propósito**:
   Implementar búsqueda de interpolación de forma iterativa.

---

### Casos en la Función

1. **Inicialización**

   ```python
   i = 0
   j = len(arr) - 1
   pos = 0
   step = 0
   ```

2. **Caso Especial de Lista con un Solo Elemento**

   ```python
   if i == j:
       if arr[i] == e:
           ...
   ```

3. **Estimación de la Posición**

   ```python
   pos = i + (((e - arr[i]) * (j - i)) // (arr[j] - arr[i]))
   ```

4. **Depuración con Mensajes DEBUG**

   ```python
   print(f"DEBUG: 'low: {i}' | 'high: {j}' | 'posicion: {pos} | 'pasos: {step}' ")
   ```

5. **Actualización de Límites**

   ```python
   elif arr[pos] < e:
       i = pos + 1
   else:
       j = pos - 1
   ```

6. **Elemento No Encontrado**

   El ciclo termina sin encontrar el elemento y no se imprime un mensaje adicional, a menos que haya una sola coincidencia inicial.

---

### Ejecución y Prueba

```python
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 11
    interpolation_search(lista, elemento)
```

---

### Salida Esperada

```plaintext
DEBUG: 'low: 0' | 'high: 11' | 'posicion: 5 | 'pasos: 0'
elemento 11 se encuentra en la posicion 5, el algoritmo lo ubico en 1 pasos
⏱️ Tiempo de ejecución: X.XXXX ms
```

---

## Estructura del Código: `interpolation_search_recursive`

### Definición de la Función

```python
def interpolation_search_recursive(arr, e, i=0, j=None, step=0):
```

1. **Parámetros**:

   * `arr`: Lista ordenada.
   * `e`: Elemento a buscar.
   * `i`: Índice inferior.
   * `j`: Índice superior.
   * `step`: Contador de pasos.

2. **Propósito**:
   Implementar búsqueda por interpolación utilizando recursividad.

---

### Casos en la Función

1. **Inicialización de `j`**

   ```python
   if j is None:
       j = len(arr) - 1
   ```

2. **Condición de Detención**

   ```python
   if i == j:
       ...
   ```

3. **Interpolación**

   ```python
   pos = i + ((e - arr[i]) * (j - i) // (arr[j] - arr[i]))
   ```

4. **Depuración con Mensajes DEBUG**

   ```python
   print(f"DEBUG: 'low: {i}' | 'high: {j}' | 'posicion: {pos} | 'step: {step}' ")
   ```

5. **Llamadas Recursivas**

   ```python
   return interpolation_search_recursive(arr, e, pos+1, j, step)
   ```

---

### Ejecución y Prueba

```python
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 11
    interpolation_search_recursive(lista, elemento)
```

---

### Salida Esperada

```plaintext
DEBUG: 'low: 0' | 'high: 11' | 'posicion: 5 | 'step: 1'
Valor encontrado en 1 step, en la posicion 5
⏱️ Tiempo de ejecución: X.XXXX ms
```

---

## Comparación entre Ambos Algoritmos

| Aspecto                  | `interpolation_search`             | `interpolation_search_recursive`   |
| ------------------------ | ---------------------------------- | ---------------------------------- |
| **Enfoque**              | Iterativo                          | Recursivo                          |
| **Estrategia**           | Estimación basada en interpolación | Estimación basada en interpolación |
| **Casos Eficientes**     | Listas uniformemente distribuidas  | Listas uniformemente distribuidas  |
| **Complejidad Promedio** | \$O(\log\log n)\$                  | \$O(\log\log n)\$                  |
| **Peor Caso**            | \$O(n)\$                           | \$O(n)\$                           |

---

## Notas Finales

1. **Requisito Principal**: La lista debe estar **ordenada** y **uniformemente distribuida** para que el algoritmo sea eficiente.
2. **Comparación con Búsqueda Binaria**:

   * Es más rápida que la binaria en datos uniformes.
   * En listas no uniformes puede degradarse.
3. **Aplicaciones Comunes**:

   * Bases de datos indexadas.
   * Sistemas de archivos optimizados para acceso predictivo.