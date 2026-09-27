# Algoritmos de Búsqueda

## ÍNDICE

Los siguientes algoritmos están ordenados de forma creciente a partir de su grado de dificultad

* [Introducción](#introducción)
* [1. Búsqueda lineal (Linear Search)](#búsqueda-lineal-linear-search)
  - [Código de ejemplo](https://github.com/gnvidal/Algorithms/blob/93dc6e423633a95cc60a16a0b3e6801b8ca24c3b/1.Searching_algorithms/1.Search_linear/Search_linear.py)
    - [Explicación del código](https://github.com/gnvidal/Algorithms/blob/efdc87170ec781c439ad154daa8cd42e776d1953/1.Searching_algorithms/1.Search_linear/Linear_search.jpg)
    - [[Programación recursiva] Código de ejemplo](https://github.com/gnvidal/Algorithms/blob/905fd25a75db603978a7fa406e68b09dda314db8/1.Searching_algorithms/1.Search_linear/Linear_search_recursive.py)
* [2. Búsqueda binaria (Binary Search)](#búsqueda-binaria-binary-search)
  - [Código de ejemplo](https://github.com/gnvidal/Algorithms/blob/55181a857c1e33bab6501782292f6bffa8ddb260/1.Searching_algorithms/2.Binary_search/Binary_search.py)
      - [Explicación del código](https://github.com/gnvidal/Algorithms/blob/55181a857c1e33bab6501782292f6bffa8ddb260/1.Searching_algorithms/2.Binary_search/Search_binary.jpg)
* [3. Búsqueda por interpolación (Interpolation Search)](#búsqueda-por-interpolación-interpolation-search)
    - [Código de ejemplo](https://github.com/gnvidal/Algorithms/blob/55181a857c1e33bab6501782292f6bffa8ddb260/1.Searching_algorithms/3.Interpolation_Search/Interpolation_Search.py)
      - [Explicación del código](https://github.com/gnvidal/Algorithms/blob/55181a857c1e33bab6501782292f6bffa8ddb260/1.Searching_algorithms/3.Interpolation_Search/interpolation_search.jpg)
* [4. Búsqueda de salto (Jump Search)](#búsqueda-de-salto-jump-search)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [5. Búsqueda exponencial (Exponential Search)](#búsqueda-exponencial-exponential-search)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [6. Búsqueda de interpolación inversa (Inverse Interpolation Search)](#búsqueda-de-interpolación-inversa-inverse-interpolation-search)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [7. Búsqueda de Fibonacci (Fibonacci Search)](#búsqueda-de-fibonacci-fibonacci-search)
  - [Código de ejemplo]()
      - [Explicación del código]()
      - [Explicación del código]()
* [8. Búsqueda por hash (Hash Search)](#búsqueda-por-hash-hash-search)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [9. Búsqueda por tabla de dispersión (Hashing with Chaining)](#búsqueda-por-tabla-de-dispersión-hashing-with-chaining)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [10. Búsqueda por tabla hash con direcciones abiertas (Hashing with Open Addressing)](#búsqueda-por-tabla-hash-con-direcciones-abiertas-hashing-with-open-addressing)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [11. Búsqueda de árbol binario (Binary Tree Search)](#búsqueda-de-árbol-binario-binary-tree-search)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [12. Búsqueda por árbol de búsqueda binario equilibrado (Balanced Binary Search Tree)](#búsqueda-por-árbol-de-búsqueda-binario-equilibrado-balanced-binary-search-tree)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [13. Búsqueda por árbol B (B-Tree)](#búsqueda-por-árbol-b-b-tree)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [14. Búsqueda en profundidad (DFS, por sus siglas en inglés)](#búsqueda-en-profundidad-dfs-por-sus-siglas-en-inglés)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [15. Búsqueda en amplitud (BFS, por sus siglas en inglés)](#búsqueda-en-amplitud-bfs-por-sus-siglas-en-inglés)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [16. Búsqueda en profundidad limitada (DLS, por sus siglas en inglés)](#búsqueda-en-profundidad-limitada-dls-por-sus-siglas-en-inglés)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [17. Búsqueda de costo uniforme (UCS, por sus siglas en inglés)](#búsqueda-de-costo-uniforme-ucs-por-sus-siglas-en-inglés)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [18. Búsqueda A (A-star)](#búsqueda-a-a-star)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [19. Búsqueda en profundidad iterativa (IDS, por sus siglas en inglés)](#búsqueda-en-profundidad-iterativa-ids-por-sus-siglas-en-inglés)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [20. Algoritmo de Dijkstra](#algoritmo-de-dijkstra)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [21. Búsqueda de salto (Jump search)](#búsqueda-de-salto-jump-search-1)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [22. Algoritmo de Bellman-Ford](#algoritmo-de-bellman-ford)
  - [Código de ejemplo]()
      - [Explicación del código]()
* [23. Algoritmo de Floyd-Warshall](#algoritmo-de-floyd-warshall)
  - [Código de ejemplo]()
      - [Explicación del código]()

# Introducción

>Los algoritmos de búsqueda son algortimos que nos permite encontrar un valor dentro de un conjunto de datos.
>Para que un algoritmo de búsqueda pueda operar sobre una lista de manera efectiva, existen ciertas condiciones que deben cumplirse:
>
>**Ordenación de la lista:** En muchos algoritmos de búsqueda eficientes, se asume que la lista está ordenada de alguna manera. Esto permite utilizar técnicas de búsqueda más rápidas, como la búsqueda binaria, en lugar de una búsqueda lineal. Si la lista no está ordenada, es posible que sea necesario realizar una etapa de ordenamiento previa para optimizar el proceso de búsqueda.
>
>**Acceso aleatorio:** Los algoritmos de búsqueda eficientes suelen requerir acceso aleatorio a los elementos de la lista. Esto significa que se puede acceder directamente a cualquier elemento de la lista utilizando su posición o índice. Si la lista no permite acceso aleatorio, como ocurre en las listas enlazadas, algunos algoritmos de búsqueda pueden no ser aplicables y sería necesario adaptar el enfoque de búsqueda.
>
>**Elementos comparables:** En la mayoría de los algoritmos de búsqueda, se comparan los elementos de la lista para determinar si coinciden con el valor buscado. Por lo tanto, los elementos de la lista deben ser comparables, lo que implica que se pueda definir una relación de orden o igualdad entre ellos. Si los elementos no son comparables, se deben utilizar técnicas de búsqueda alternativas o se debe adaptar el algoritmo para trabajar con el tipo de datos específico.
>
>**Tamaño y complejidad:** El tamaño de la lista y la complejidad de los elementos también son factores importantes a tener en cuenta al seleccionar un algoritmo de búsqueda. Algunos algoritmos son más adecuados para listas pequeñas o para búsquedas en tiempo real, mientras que otros son más eficientes en listas grandes o en escenarios con requerimientos de recursos específicos.
>
>En resumen, las condiciones clave para un algoritmo de búsqueda efectivo en una lista son: ordenación (si es necesario), acceso aleatorio a los elementos, comparabilidad de los elementos y consideración del tamaño y complejidad de la lista. 

## Algoritmos de búsqueda para listas de un vector 

* ### **Búsqueda lineal (Linear Search)**

Compara cada elemento de manera secuencial con el valor buscado. Es simple pero puede ser ineficiente para grandes conjuntos de datos no ordenados.

[[Ejemplo de código](https://github.com/gnvidal/Algorithms/blob/93dc6e423633a95cc60a16a0b3e6801b8ca24c3b/1.Searching_algorithms/1.Search_linear/Search_linear.py)]

[[Explicación del código](https://github.com/gnvidal/Algorithms/blob/93dc6e423633a95cc60a16a0b3e6801b8ca24c3b/1.Searching_algorithms/1.Search_linear/Linear_search.jpg)]

* ### **Búsqueda binaria (Binary Search)**
Solo aplicable a conjuntos de datos ordenados. Divide el conjunto a la mitad en cada iteración, eliminando la mitad de los elementos en cada paso. Es más eficiente que la búsqueda lineal.

[[Ejemplo de código](https://github.com/gnvidal/Algorithms/blob/76d921a4c6f78b6c2e39ba693631a83a44820bfc/1.Searching_algorithms/2.Searching_binary.py)]

[[Explicación del código](https://github.com/gnvidal/Algorithms/blob/93dc6e423633a95cc60a16a0b3e6801b8ca24c3b/1.Searching_algorithms/2.Binary_search/Search_binary.jpg)]

* ### **Búsqueda por interpolación (Interpolation Search)**

Similar a la búsqueda binaria, pero utiliza una estimación interpolada para determinar la ubicación probable del elemento buscado. Es más rápida que la búsqueda binaria para conjuntos de datos uniformemente distribuidos.

[[Ejemplo del código](https://github.com/gnvidal/Algorithms/blob/36bdd2f9e2c6f88d288c77e5a3589eb54b456aa0/1.Searching_algorithms/3.Interpolation_Search/Interpolation_Search.py)]

[[Explicación del código](https://github.com/gnvidal/Algorithms/blob/55181a857c1e33bab6501782292f6bffa8ddb260/1.Searching_algorithms/3.Interpolation_Search/interpolation_search.jpg)]

* ### **Búsqueda de salto (Jump Search)**

Funciona saltando hacia adelante en bloques fijos en lugar de comparar cada elemento. Requiere que los datos estén ordenados y es más eficiente que la búsqueda lineal.

* ### **Búsqueda exponencial (Exponential Search)**

Comienza con un rango pequeño y lo expande exponencialmente hasta encontrar un rango que contenga el elemento buscado. Luego, realiza una búsqueda binaria en ese rango. Es eficiente para conjuntos de datos ordenados y no ordenados.

* ### **Búsqueda de interpolación inversa (Inverse Interpolation Search)** 

Una variante de la búsqueda por interpolación que se aplica cuando los datos están distribuidos de manera no uniforme y se conoce la función inversa de distribución.

* ### **Búsqueda de Fibonacci (Fibonacci Search)**

Utiliza la secuencia de Fibonacci para dividir el conjunto de datos en segmentos. Es similar a la búsqueda binaria pero puede tener un mejor rendimiento en ciertos casos.

* ### **Búsqueda por hash (Hash Search)**

Utiliza una función hash para almacenar los elementos en una estructura de datos especializada (como una tabla hash). La búsqueda se realiza calculando el hash del valor deseado y localizando rápidamente el elemento correspondiente.

* ### **Búsqueda por tabla de dispersión (Hashing with Chaining)**

Utiliza una tabla de dispersión (hash table) para almacenar y buscar elementos. Cada elemento se asigna a un "bucket" en la tabla utilizando una función hash, y los elementos con colisiones se almacenan en una lista enlazada.

* ### **Búsqueda por tabla hash con direcciones abiertas (Hashing with Open Addressing)**

Es otra variante de la búsqueda por tabla de dispersión donde las colisiones se resuelven mediante el uso de una secuencia determinada de posiciones alternativas en la tabla.

## Algoritmos de búsqueda para grafos

* ### **Búsqueda de árbol binario (Binary Tree Search)**

Utiliza un árbol binario de búsqueda para organizar los datos de manera que la búsqueda se realice de manera eficiente en tiempo logarítmico. Requiere la construcción previa del árbol.

* ### **Búsqueda por árbol de búsqueda binario equilibrado (Balanced Binary Search Tree)**

Es una variante del árbol binario de búsqueda que garantiza un balanceo adecuado del árbol para mejorar aún más la eficiencia de búsqueda. Ejemplos de árboles equilibrados incluyen el árbol AVL y el árbol Rojo-Negro.

* ### **Búsqueda por árbol B (B-Tree)**

Es una estructura de datos en árbol ampliamente utilizada para la búsqueda eficiente en bases de datos y sistemas de archivos. Los árboles B permiten un acceso rápido a los elementos y son adecuados para almacenar grandes cantidades de datos ordenados.

* ### **Búsqueda en profundidad (DFS, por sus siglas en inglés)**

Explora un grafo siguiendo las aristas lo más profundamente posible antes de retroceder. Es relativamente fácil de implementar utilizando recursión o una pila.

* ### **Búsqueda en amplitud (BFS, por sus siglas en inglés)**

Explora un grafo nivel por nivel, expandiendo todos los nodos vecinos antes de avanzar al siguiente nivel. Se puede implementar utilizando una cola.

* ### **Búsqueda en profundidad limitada (DLS, por sus siglas en inglés)**

Similar a DFS, pero limita la profundidad máxima de búsqueda. Ayuda a evitar la búsqueda infinita en grafos con ciclos o profundidades desconocidas.

* ### **Búsqueda de costo uniforme (UCS, por sus siglas en inglés)**

Encuentra la ruta más corta en un grafo ponderado asignando un costo a cada arista. Utiliza una cola de prioridad ordenada por el costo acumulado hasta cada nodo.

* ### **Búsqueda A (A-star)**

Combina la búsqueda de costo uniforme con una heurística que estima el costo restante para alcanzar el objetivo. Utiliza una función de evaluación que considera el costo acumulado y la heurística para seleccionar el siguiente nodo a explorar. Requiere una heurística admisible y consistente para garantizar la optimización.

* ### **Búsqueda en profundidad iterativa (IDS, por sus siglas en inglés)**

Es una estrategia que combina la profundidad de búsqueda limitada y la búsqueda en profundidad. Aumenta gradualmente el límite de profundidad hasta encontrar la solución.

* ### **Algoritmo de Dijkstra**

Encuentra el camino más corto desde un nodo fuente hasta todos los demás nodos en un grafo ponderado no negativo. Utiliza una cola de prioridad para seleccionar los nodos con menor costo.

* ### **Búsqueda de salto (Jump search)**

Es una técnica que combina la búsqueda lineal con saltos hacia adelante en un grafo ordenado. Ayuda a reducir el número de comparaciones necesarias.

* ### **Algoritmo de Bellman-Ford**

Encuentra el camino más corto desde un nodo fuente hasta todos los demás nodos en un grafo ponderado que puede contener aristas de peso negativo. Utiliza relajación iterativa para actualizar los costos de los nodos.

* ### **Algoritmo de Floyd-Warshall**

Encuentra todos los caminos más cortos entre todos los pares de nodos en un grafo ponderado con o sin ciclos negativos. Utiliza una matriz de distancias para mantener el costo acumulado entre los nodos.
