# Propuesta de reorganización — repositorio `Algorithms`

**Estado:** solo propuesta. No se ha movido, creado ni borrado nada.

## 1. Reglas

- Los directorios de raíz van **numerados** por orden académico (de lo básico a lo avanzado).
- Cada script se ubica por el **tema que enseña**.
- `400_ejercicios_python/` queda **intacto**: mismo nombre, mismos subdirectorios, mismos archivos.
- **No se borra ningún script existente** y sus nombres se conservan (salvo lo indicado en §6).
- Scripts **nuevos**: solo se deja el **nombre del archivo** (`.py` vacío) para que tú lo desarrolles. Aparecen marcados `[NUEVO]`. No escribo su contenido.
- `02-programacion-orientada-a-objetos/` se crea **sin ningún script**. Solo lleva su `README.md`.
- Cada carpeta (raíz incluida) lleva un `README.md`. Aparecen marcados `[README]`.

Leyenda: `[NUEVO]` = archivo vacío que rellenas tú · `[README]` = README nuevo · `(→ origen)` = de dónde viene el archivo.

## 2. Orden de los directorios de raíz

| Nº | Directorio | Área |
|---|---|---|
| 01 | `01-fundamentos-de-programacion` | Primer año: variables, condicionales, ciclos, funciones, archivos |
| 02 | `02-programacion-orientada-a-objetos` | Clases y objetos (vacío, tuyo) |
| 03 | `03-estructuras-de-datos` | Cómo organizar datos en memoria |
| 04 | `04-algoritmos` | Búsqueda, ordenamiento, recursividad, grafos, técnicas |
| 05 | `05-matematicas-computacionales` | Teoría de números, fractales |
| 06 | `06-inteligencia-artificial` | Algoritmos genéticos |
| 07 | `07-arquitectura-y-logica-digital` | Puertas lógicas |
| 08 | `08-herramientas-y-automatizacion` | Scripts de utilidad |
| — | `400_ejercicios_python` | Colección externa, sin cambios |
| — | `assets` | Imágenes del repositorio |

## 3. Árbol completo

```
Algorithms/
├── README.md                                           [README]  (índice general, reemplaza al actual)
├── LICENSE
├── requirements.txt
├── .gitignore
├── .vscode/settings.json
├── assets/
│   └── kimelfe.PNG                                     (→ raíz)
│
├── 01-fundamentos-de-programacion/
│   ├── README.md                                       [README]  (→ absorbe 01.Miscellaneous/README.md)
│   ├── 01-entrada-salida-y-operaciones/
│   │   ├── README.md                                   [README]
│   │   ├── 01.py                                       (→ 01.Miscellaneous/01. Control secuenciales/)
│   │   ├── 02.py
│   │   ├── 03.py
│   │   ├── 04.py
│   │   ├── 05.py
│   │   ├── 06.py
│   │   ├── 07.py
│   │   ├── 08.py
│   │   ├── 01.area_pintura.py                          (→ 01.Miscellaneous/)
│   │   ├── 01.exercise1.py                             (→ 01.Miscellaneous/)
│   │   ├── 01.currency_converter.py                    (→ 01.Miscellaneous/)
│   │   ├── 02.currency_converter_various.py            (→ 01.Miscellaneous/)
│   │   ├── 05.telegrafo.py                             (→ 01.Miscellaneous/)
│   │   └── recursive_origen_01.exercise1.py            (→ 06.Recursive/01.exercise1.py, ver §6)
│   ├── 02-condicionales/
│   │   ├── README.md                                   [README]
│   │   ├── 09.py                                       (→ 01. Control secuenciales/)
│   │   ├── 10.py
│   │   ├── 11.py
│   │   ├── 12.py
│   │   ├── 13.py
│   │   ├── 14.py
│   │   ├── 15.py
│   │   ├── 02.exercise2.py                             (→ 01.Miscellaneous/)
│   │   ├── 02.Nota_promedio_clasificacion.py           (→ 01.Miscellaneous/)
│   │   ├── 03.nota_promedio_clasificacion.py           (→ 01.Miscellaneous/)
│   │   ├── aprobacion-credito.py                       (→ 01.Miscellaneous/)
│   │   ├── 10.is_leap.py                               (→ 01.Miscellaneous/, archivo vacío)
│   │   └── recursive_origen_02.exercise2.py            (→ 06.Recursive/02.exercise2.py, ver §6)
│   ├── 03-ciclos/
│   │   ├── README.md                                   [README]
│   │   ├── 16.py                                       (→ 01.Miscellaneous/02. Ciclo while/)
│   │   ├── 17.py
│   │   ├── 18.py
│   │   ├── ciclo_while.py                              (→ 01.Miscellaneous/)
│   │   ├── 03.py  → renombrar a 03_cajero_automatico.py (→ 01.Miscellaneous/03.py, ver §6)
│   │   ├── billetera-estudiantil.py                    (→ 01.Miscellaneous/)
│   │   ├── Calculo-promedio-nota.py                    (→ 01.Miscellaneous/)
│   │   ├── cuestionario-ciencia-ficcion.py             (→ 01.Miscellaneous/)
│   │   └── moda-mediana-entero.py                      (→ 01.Miscellaneous/)
│   ├── 04-cadenas-de-texto/
│   │   ├── README.md                                   [README]
│   │   ├── 04.palindrome.py                            (→ 01.Miscellaneous/)
│   │   ├── 06.consonant_or_vocal.py                    (→ 01.Miscellaneous/)
│   │   ├── 06.telegrafo1.py                            (→ 01.Miscellaneous/, casi vacío: 23 bytes)
│   │   ├── 07.jerigonzo.py                             (→ 01.Miscellaneous/, archivo vacío)
│   │   ├── contar_vocales.py                           [NUEVO]
│   │   ├── invertir_cadena.py                          [NUEVO]
│   │   └── anagramas.py                                [NUEVO]
│   ├── 05-funciones/
│   │   ├── README.md                                   [README]
│   │   ├── 03.currency_converter_def.py                (→ 01.Miscellaneous/)
│   │   ├── funcion_con_parametros_por_defecto.py       [NUEVO]
│   │   └── funciones_lambda.py                         [NUEVO]
│   ├── 06-manejo-de-archivos/
│   │   ├── README.md                                   [README]
│   │   ├── BDD-calculo-IMC.py                          (→ 01.Miscellaneous/, usa open() en lectura y escritura)
│   │   ├── leer_archivo_de_texto.py                    [NUEVO]
│   │   ├── escribir_archivo_de_texto.py                [NUEVO]
│   │   └── leer_y_escribir_csv.py                      [NUEVO]
│   └── 07-patrones-y-figuras/
│       ├── README.md                                   [README]
│       ├── 07.box_sequence_asterisk.py                 (→ 01.Miscellaneous/)
│       ├── 7.secuence.asterisk.py                      (→ 01.Miscellaneous/)
│       ├── 08.increansing_secuence_asterisk.py         (→ 01.Miscellaneous/)
│       ├── 09.secuence.asterisk.inverse.py             (→ 01.Miscellaneous/, archivo vacío)
│       ├── piramide_de_asteriscos.py                   [NUEVO]
│       └── rombo_de_asteriscos.py                      [NUEVO]
│
├── 02-programacion-orientada-a-objetos/
│   └── README.md                                       [README]  (sin scripts; tus ejercicios los agregas tú)
│
├── 03-estructuras-de-datos/
│   ├── README.md                                       [README]
│   ├── 01-listas-enlazadas/
│   │   ├── README.md                                   [README]
│   │   ├── python/
│   │   │   ├── 3-lista-enlazada.py                     (→ 1.data-structures/linked-list/python/)
│   │   │   ├── 3-lista-enlazada-poo.py
│   │   │   ├── 4-lista-doblemente-enlazada.py
│   │   │   └── lista-doblemente-enlazado.png           (→ linked-list/)
│   │   └── c/
│   │       ├── 1-ubicacion-y-espacio.c                 (→ linked-list/c/)
│   │       ├── 2.linked-list-8bytes.c
│   │       └── bin/
│   │           ├── 1.exe                               (→ linked-list/output/)
│   │           └── 2.linked-list-8bytes.exe
│   ├── 02-pilas-y-colas/
│   │   ├── README.md                                   [README]
│   │   ├── pila.py                                     [NUEVO]
│   │   └── cola.py                                     [NUEVO]
│   ├── 03-arboles/
│   │   ├── README.md                                   [README]
│   │   ├── arbol_binario.py                            [NUEVO]
│   │   └── arbol_binario_de_busqueda.py                [NUEVO]
│   └── 04-tablas-hash/
│       ├── README.md                                   [README]
│       └── tabla_hash.py                               [NUEVO]
│
├── 04-algoritmos/
│   ├── README.md                                       [README]
│   ├── 01-busqueda/
│   │   ├── README.md                                   (→ 1.Searching_algorithms/README.md)
│   │   ├── 01-lineal/
│   │   │   ├── README.md                               (→ 1.Search_linear/)
│   │   │   ├── Search_linear.py
│   │   │   ├── Linear_search_recursive.py
│   │   │   ├── test.py
│   │   │   └── linear-search.png
│   │   ├── 02-binaria/
│   │   │   ├── README.md                               (→ 2.Binary_search/)
│   │   │   ├── Binary_search.py
│   │   │   ├── Binary_search_recursive.py
│   │   │   ├── test.py
│   │   │   ├── Binary_search.jpg
│   │   │   └── binary-search.png
│   │   ├── 03-interpolacion/
│   │   │   ├── README.md                               (→ 3.Interpolation_Search/)
│   │   │   ├── Interpolation_Search.py
│   │   │   ├── interpolation_search_recursive.py
│   │   │   ├── test.py
│   │   │   └── interpolation_search.png
│   │   ├── 04-salto/
│   │   │   ├── README.md                               [README]  (4.Jump_search no tiene)
│   │   │   ├── Jump_search.py                          (→ 4.Jump_search/)
│   │   │   ├── Jump_search_recursive.py
│   │   │   ├── Jump_search.jpg
│   │   │   └── test.py                                 [NUEVO]
│   │   └── 05-exponencial/
│   │       ├── README.md                               [README]  (5.exponencial_search no tiene)
│   │       ├── exponencial_search.py                   (→ 5.exponencial_search/)
│   │       ├── exponencial_search_recursive.py
│   │       └── test.py                                 [NUEVO]
│   ├── 02-ordenamiento/
│   │   ├── README.md                                   [README]
│   │   ├── burbuja.py                                  [NUEVO]
│   │   ├── seleccion.py                                [NUEVO]
│   │   ├── insercion.py                                [NUEVO]
│   │   ├── merge_sort.py                               [NUEVO]
│   │   └── quick_sort.py                               [NUEVO]
│   ├── 03-recursividad/
│   │   ├── README.md                                   (→ 06.Recursive/README.md)
│   │   ├── 000.example-fibonacci-iterative.py          (→ 06.Recursive/)
│   │   ├── 001.example-fibonacci-recursive.py
│   │   ├── 002.example-fibonacci.py
│   │   ├── 01.exercises.py
│   │   ├── 02.exercises.py
│   │   ├── 03.exercises.py
│   │   ├── 04.exercise.py
│   │   ├── 05.exercises-iterative.py
│   │   ├── 05.exercises-recursive.py
│   │   ├── 06.exercise.py
│   │   ├── 07.exercise.py
│   │   ├── 08.exercises-iterativo.py
│   │   ├── 08.exercises-recursive.py
│   │   ├── 09.exercise-iterative.py
│   │   ├── 09.exercise-recursive.py
│   │   ├── 05.palindorme_recursive.py                  (→ 01.Miscellaneous/)
│   │   ├── torres_de_hanoi.py                          [NUEVO]
│   │   └── backtracking_n_reinas.py                    [NUEVO]
│   ├── 04-grafos/
│   │   ├── README.md                                   [README]
│   │   ├── ruta-mas-corta.py                           (→ Grafos/)
│   │   ├── busqueda_en_anchura_bfs.py                  [NUEVO]
│   │   └── busqueda_en_profundidad_dfs.py              [NUEVO]
│   └── 05-tecnicas-de-resolucion/
│       ├── README.md                                   [README]
│       ├── dos-apuntadores/
│       │   ├── README.md                               (→ dos-apuntadores/)
│       │   └── ejemplo_dos_apuntadores.py              [NUEVO]
│       ├── merge-two-sorted-lists/
│       │   ├── README.md                               (→ merge-two-sorted-lists/)
│       │   ├── merge_lists_module.py
│       │   ├── test.py
│       │   └── merge-lists.png
│       └── Verifying-Alien-Dictionary/
│           ├── README.md                               (→ Verifying-Alien-Dictionary/)
│           ├── alien_dictionary.py
│           ├── test.py
│           └── photo-alien.png
│
├── 05-matematicas-computacionales/
│   ├── README.md                                       [README]
│   ├── 01-teoria-de-numeros/
│   │   ├── README.md                                   [README]
│   │   ├── 04.perfect_number.py                        (→ 01.Miscellaneous/)
│   │   ├── numeros_primos.py                           [NUEVO]
│   │   └── maximo_comun_divisor.py                     [NUEVO]
│   └── 02-fractales/
│       ├── README.md                                   [README]
│       └── fractal.py                                  (→ 01.Miscellaneous/)
│
├── 06-inteligencia-artificial/
│   ├── README.md                                       [README]
│   └── 01-algoritmos-geneticos/
│       ├── README.md                                   [README]
│       └── 1.guess_password.py                         (→ 03.Algorithms_genetic/)
│
├── 07-arquitectura-y-logica-digital/
│   ├── README.md                                       [README]
│   └── 01-puertas-logicas/
│       ├── README.md                                   (→ logic-gates/)
│       ├── gates.py
│       ├── main.py
│       ├── logic-gates.png
│       └── conversor_decimal_binario.py                [NUEVO]
│
├── 08-herramientas-y-automatizacion/
│   ├── README.md                                       [README]
│   ├── 0.Download_youtube.py                           (→ 07. Tools/)
│   ├── automate-email-sending.py
│   ├── automate-file-sorting.py
│   └── git-automation.py
│
└── 400_ejercicios_python/                              (INTACTO)
    ├── 00.400-ejercicios.pdf
    ├── README.md
    ├── 01.variables-operadores-expresiones-condicionales-bucles/   (13 archivos)
    ├── 02.funciones/                                               (23 archivos)
    ├── 03.listas-tuplas-conjuntos-diccionarios/                    (40 archivos)
    ├── 03.POO/                                                     (18 archivos)
    ├── 08.Recursividad/                                            (148–152, 5 archivos)
    └── listas-enlazadas/                                           (188, 189)
```

## 4. Qué directorios actuales desaparecen

`01.Miscellaneous/` (con `01. Control secuenciales/` y `02. Ciclo while/`), `03.Algorithms_genetic/`, `06.Recursive/`, `07. Tools/`, `1.data-structures/`, `1.Searching_algorithms/`, `Grafos/`, `dos-apuntadores/`, `logic-gates/`, `merge-two-sorted-lists/`, `Verifying-Alien-Dictionary/`. Todos sus archivos aparecen arriba con `(→ origen)`. Ninguno queda sin destino.

## 5. Scripts nuevos, resumen (`[NUEVO]`: solo el nombre, archivo vacío)

| Carpeta | Archivos |
|---|---|
| `01/04-cadenas-de-texto` | `contar_vocales.py`, `invertir_cadena.py`, `anagramas.py` |
| `01/05-funciones` | `funcion_con_parametros_por_defecto.py`, `funciones_lambda.py` |
| `01/06-manejo-de-archivos` | `leer_archivo_de_texto.py`, `escribir_archivo_de_texto.py`, `leer_y_escribir_csv.py` |
| `01/07-patrones-y-figuras` | `piramide_de_asteriscos.py`, `rombo_de_asteriscos.py` |
| `03/02-pilas-y-colas` | `pila.py`, `cola.py` |
| `03/03-arboles` | `arbol_binario.py`, `arbol_binario_de_busqueda.py` |
| `03/04-tablas-hash` | `tabla_hash.py` |
| `04/01-busqueda/04-salto` | `test.py` |
| `04/01-busqueda/05-exponencial` | `test.py` |
| `04/02-ordenamiento` | `burbuja.py`, `seleccion.py`, `insercion.py`, `merge_sort.py`, `quick_sort.py` |
| `04/03-recursividad` | `torres_de_hanoi.py`, `backtracking_n_reinas.py` |
| `04/04-grafos` | `busqueda_en_anchura_bfs.py`, `busqueda_en_profundidad_dfs.py` |
| `04/05-tecnicas.../dos-apuntadores` | `ejemplo_dos_apuntadores.py` |
| `05/01-teoria-de-numeros` | `numeros_primos.py`, `maximo_comun_divisor.py` |
| `07/01-puertas-logicas` | `conversor_decimal_binario.py` |

Total: 30 archivos vacíos. `02-programacion-orientada-a-objetos/` no lleva ninguno. Si alguno no te interesa, lo saco antes de ejecutar.

## 6. Renombres y casos especiales

Solo hay tres, para evitar choques o confusión:
1. `01.Miscellaneous/03.py` (simulador de cajero con `while`) se llamaría `03_cajero_automatico.py`. Choca con `01. Control secuenciales/03.py` al estar en carpetas hermanas y no quiero que se confundan.
2. `06.Recursive/01.exercise1.py` y `02.exercise2.py` no usan recursión (áreas de paredes y promedio de notas). Van a fundamentos con prefijo `recursive_origen_` para que no choquen con los homónimos de `01.Miscellaneous`. Si prefieres dejarlos en `03-recursividad`, se cambia.
3. Los `README.md` que hoy existen se conservan en su carpeta nueva (§3). Solo el de `01.Miscellaneous` se fusiona en el de `01-fundamentos-de-programacion`.

Todo lo demás conserva el nombre original.

## 7. Datos verificados

- Vacíos (0 bytes): `07.jerigonzo.py`, `09.secuence.asterisk.inverse.py`, `10.is_leap.py`. `06.telegrafo1.py` tiene 23 bytes.
- Los duplicados (`01.area_pintura.py`/`01.exercise1.py`, `02.exercise2.py`/`02.Nota_promedio_clasificacion.py`, ambos conversores) siguen sin comprobar. Se comprueban con `cmp` al ejecutar.
- `kimelfe.PNG` aparece borrado del árbol de trabajo (sigue en git). Hay que restaurarlo antes de moverlo a `assets/`.

## 8. Al ejecutar (con tu aprobación)

1. Restaurar `kimelfe.PNG` con `git restore`.
2. `git mv` por área, un commit por área.
3. Crear los 30 `.py` vacíos y los README.
4. Revisar imports y rutas (`open(...)`, `import gates`, los `test.py`) que dependan de la ubicación.
5. Los bugs preexistentes no se tocan.

## 9. Decisiones abiertas

- ¿Los 30 nombres nuevos te sirven, o quitas/agregas?
- ¿Los README de las carpetas nuevas van con solo el temario, o también con una lista de ejercicios sugeridos?
