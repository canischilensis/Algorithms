# Algorithms

Colección de scripts en Python (y algo de C) para estudiar Informática, organizada como una malla curricular: cada carpeta agrupa los scripts por el tema que enseñan, de lo básico a lo avanzado.

## Estructura

| Carpeta | Contenido |
|---|---|
| [`01-fundamentos-de-programacion`](01-fundamentos-de-programacion/) | Entrada y salida, condicionales, ciclos, cadenas, funciones, archivos y patrones |
| [`02-programacion-orientada-a-objetos`](02-programacion-orientada-a-objetos/) | Clases y objetos (espacio reservado) |
| [`03-estructuras-de-datos`](03-estructuras-de-datos/) | Listas enlazadas, pilas y colas, árboles, tablas hash |
| [`04-algoritmos`](04-algoritmos/) | Búsqueda, ordenamiento, recursividad, grafos y técnicas de resolución |
| [`05-matematicas-computacionales`](05-matematicas-computacionales/) | Teoría de números y fractales |
| [`06-inteligencia-artificial`](06-inteligencia-artificial/) | Algoritmos genéticos |
| [`07-arquitectura-y-logica-digital`](07-arquitectura-y-logica-digital/) | Puertas lógicas y sistema binario |
| [`08-herramientas-y-automatizacion`](08-herramientas-y-automatizacion/) | Scripts de utilidad y automatización |
| [`400_ejercicios_python`](400_ejercicios_python/) | Colección de 400 ejercicios resueltos, con su propia numeración |

Cada carpeta tiene su propio `README.md` con los temas que cubre y la lista de scripts. Los archivos marcados como "Por desarrollar" son scripts vacíos pendientes de implementar.

## Dónde dejar un script nuevo

| Si el script trata de... | Va en |
|---|---|
| `input`, `print`, fórmulas, conversiones | `01-fundamentos-de-programacion/01-entrada-salida-y-operaciones` |
| `if / elif / else` | `01-fundamentos-de-programacion/02-condicionales` |
| `while`, acumuladores, menús | `01-fundamentos-de-programacion/03-ciclos` |
| Texto, palíndromos, vocales | `01-fundamentos-de-programacion/04-cadenas-de-texto` |
| Funciones definidas por el usuario | `01-fundamentos-de-programacion/05-funciones` |
| Leer o escribir archivos | `01-fundamentos-de-programacion/06-manejo-de-archivos` |
| Figuras con asteriscos | `01-fundamentos-de-programacion/07-patrones-y-figuras` |
| Clases, herencia, polimorfismo | `02-programacion-orientada-a-objetos` |
| Nodos, pilas, colas, árboles, tablas hash | `03-estructuras-de-datos/<estructura>` |
| Buscar un elemento | `04-algoritmos/01-busqueda/<método>` |
| Ordenar | `04-algoritmos/02-ordenamiento` |
| Una función que se llama a sí misma | `04-algoritmos/03-recursividad` |
| Nodos y aristas, caminos | `04-algoritmos/04-grafos` |
| Problemas tipo entrevista | `04-algoritmos/05-tecnicas-de-resolucion` |
| Números primos, MCD, fractales | `05-matematicas-computacionales` |
| Algoritmos genéticos | `06-inteligencia-artificial` |
| AND, OR, NOT, binario | `07-arquitectura-y-logica-digital` |
| Descargas, correo, archivos, git | `08-herramientas-y-automatizacion` |

Si un script podría ir en varias carpetas, va en el tema principal que enseña.

## Requisitos

- Python 3.x
- Dependencias de algunos scripts: `pip install -r requirements.txt`

## Uso

```bash
git clone https://github.com/Caupolicanafulvicollis/Algorithms.git
cd Algorithms
python 04-algoritmos/01-busqueda/02-binaria/Binary_search.py
```

## Licencia

MIT. Ver [`LICENSE`](LICENSE).
