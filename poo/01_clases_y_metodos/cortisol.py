"""
Ejercicio 1 — Cortisol.

Modelo: el cortisol como clase. Concentracion en microg/dL, hora del dia (0-23).
Metodos pregunta: es_pico_matutino, suprime_hipotalamo.
Metodo accion: reportar (imprime estado).
"""


class Cortisol:
    def __init__(self, concentracion_inicial, hora):
        self._validar(concentracion_inicial, hora)
        self.nombre = "cortisol"
        self.concentracion = concentracion_inicial
        self.hora = hora

    @staticmethod
    def _validar(concentracion, hora):
        if not isinstance(concentracion, (int, float)):
            raise TypeError("concentracion_inicial debe ser numerico")
        if not isinstance(hora, int):
            raise TypeError("hora debe ser int")
        if concentracion < 0:
            raise ValueError(
                f"la concentracion no puede ser negativa (recibi {concentracion})"
            )
        if not 0 <= hora <= 23:
            raise ValueError(f"hora debe estar entre 0 y 23 (recibi {hora})")

    # --- metodos pregunta (devuelven un valor, no imprimen) ---

    def es_pico_matutino(self):
        """Devuelve True si la hora esta entre 6 y 10 inclusive."""
        return 6 <= self.hora <= 10

    def suprime_hipotalamo(self):
        """Devuelve True si la concentracion supera 15 microg/dL."""
        return self.concentracion > 15

    # --- metodo accion (imprime, no devuelve) ---

    def reportar(self):
        """Imprime el estado del cortisol en una linea."""
        pico = "si" if self.es_pico_matutino() else "no"
        supr = "si" if self.suprime_hipotalamo() else "no"
        print(f"cortisol: {self.concentracion:.2f} microg/dL a las {self.hora}h")
        print(f"  pico matutino: {pico}")
        print(f"  suprime hipotalamo: {supr}")


# --- prueba ---

if __name__ == "__main__":
    c1 = Cortisol(18.0, 7)
    c1.reportar()
    print()
    c2 = Cortisol(5.0, 22)
    c2.reportar()
