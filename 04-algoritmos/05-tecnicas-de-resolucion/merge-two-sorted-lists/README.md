# Merge Lists - Combinación de Listas Ordenadas

![Merge Lists](merge-lists.png)

## Descripción del Proyecto

Este repositorio presenta una solución al problema clásico de combinación o fusión (**merge**) de dos listas ordenadas en una sola lista ordenada, habitual en entrevistas técnicas para empresas como Google, Amazon y Microsoft. El objetivo es integrar los elementos de la segunda lista en la primera lista, manteniendo el orden ascendente.

## Planteamiento del Problema

* **Entradas**:

  * `nums1`: primera lista ordenada con espacio suficiente al final para contener la segunda lista (ceros adicionales).
  * `m`: número de elementos iniciales válidos en `nums1`.
  * `nums2`: segunda lista ordenada.
  * `n`: número de elementos válidos en `nums2`.

* **Salida**:

  * Lista ordenada combinada dentro de `nums1`.

## Solución en Python

```python
def merge_lists(nums1, m, nums2, n):
    p = (m + n) - 1
    p1 = m - 1
    p2 = n - 1

    while 0 <= p1 and 0 <= p2:
        if nums1[p1] < nums2[p2]:
            nums1[p1] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1

    if n != m:
        nums1[:p2 + 1] = nums2[:p2 + 1]

    return nums1
```

### Ejemplo de uso

```python
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3

    resultado = merge_lists(nums1, m, nums2, n)
    print("Lista combinada:", resultado)  # → [1, 2, 2, 3, 5, 6]
```

## Análisis de Complejidad

* **Tiempo:** O(m + n)
  * m = número de elementos válidos en la primera lista.
  * n = número de elementos válidos en la segunda lista.

* **Espacio extra:** O(1) (no se requiere espacio adicional significativo).

## Importancia del Ejercicio

* Refuerza técnicas para manipular listas ordenadas eficientemente.
* Evalúa habilidades en el manejo de índices múltiples (técnica de dos punteros).
* Muy común en entrevistas para evaluar la capacidad de escribir código eficiente en espacio y tiempo.

## Consejos Prácticos

1. Siempre inicia desde el final de ambas listas para evitar problemas de sobrescritura.
2. Maneja cuidadosamente los índices para evitar errores de límites.
3. Realiza pruebas con casos donde una lista esté completamente contenida en otra o tenga valores negativos.
4. Asegúrate de entender completamente la técnica de dos punteros antes de implementar la solución.