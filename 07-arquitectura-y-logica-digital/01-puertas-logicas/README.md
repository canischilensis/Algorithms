# 🔌 Simulador Lógico de Puertas Digitales

![logic-gates](logic-gates.png)

## 📘 Descripción del Proyecto

Este repositorio contiene una implementación en Python de puertas lógicas digitales básicas (AND, OR, NOT, NAND, NOR, XOR, XNOR) y su uso en un sistema de simulación lógica. El objetivo es comprender el funcionamiento de las compuertas y cómo se combinan en circuitos digitales.

## 🧠 Planteamiento del Problema

En la computación digital, las compuertas lógicas forman la base de cualquier circuito. Este proyecto simula dichas puertas, permitiendo ejecutar combinaciones lógicas sobre valores binarios (0 y 1).

### 🟢 Entradas:

* Tres valores binarios (`val1`, `val2`, `val3`), cada uno siendo `0` o `1`.

### 🔴 Salidas:

* Resultado de un circuito lógico que aplica:

  * `(val1 OR val2) AND (NOT val3)`

## ⚙️ Scripts Principales

### `gates.py`

Contiene la definición y pruebas de las siguientes compuertas lógicas:

* `logic_and(val1, val2)`
* `logic_or(val1, val2)`
* `logic_not(val)`
* `logic_nand(val1, val2)`
* `logic_nor(val1, val2)`
* `logic_xor(val1, val2)`
* `logic_xnor(val1, val2)`

Incluye pruebas unitarias básicas utilizando `assert` para validar la lógica.

### `main.py`

Simula un circuito lógico compuesto con tres entradas. Ejecuta:

```python
circuit_1 = logic_and(logic_or(val1, val2), logic_not(val3))
```

Itera sobre todas las combinaciones posibles de entrada (`0` y `1`) e imprime el resultado.

## 🖥️ Ejecución

Para correr la simulación, asegúrate de tener Python 3 instalado y ejecuta:

```bash
python main.py
```

La salida mostrará todas las combinaciones posibles de los valores de entrada y el resultado del circuito lógico.

## 🧪 Testeo

Puedes verificar el correcto funcionamiento de las compuertas ejecutando:

```bash
python gates.py
```

Si todos los tests son exitosos, verás:

```
Test para logic: todos los gates han sido existosos
```

## 📂 Estructura del Proyecto

```
.
├── gates.py       # Definición de puertas lógicas y pruebas
├── main.py        # Simulación del circuito lógico
└── README.md      # Documentación del proyecto
```

## 🚀 Futuras Mejoras

* Implementación de circuitos lógicos más complejos.
* Interfaz gráfica para simular puertas lógicas.
* Visualización de los resultados en tablas de verdad.