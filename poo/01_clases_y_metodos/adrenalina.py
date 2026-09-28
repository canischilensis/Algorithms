"""
Ejercicio 2 — Adrenalina.

Modelo: adrenalina con decaimiento exponencial.
Vida media: 2 minutos. Umbral fisiologico: 0.05 ng/mL.
Metodo accion: transcurrir_minutos (modifica concentracion), reportar.
Metodo pregunta: es_fisiologicamente_activa.
"""


class Adrenalina:
    def __init__(self, concentracion_inicial):
        self._validar(concentracion_inicial)
        self.nombre = "adrenalina"
        self.concentracion = concentracion_inicial
        self.vida_media_min = 2.0

    @staticmethod
    def _validar(concentracion_inicial):
        if not isinstance(concentracion_inicial, (int, float)):
            raise TypeError("concentracion inicial debe ser numerico")
        if concentracion_inicial < 0:
            raise ValueError(
                f"la concentracion no puede ser negativa (recibi {concentracion_inicial})"
            )

    # --- metodo pregunta ---

    def es_fisiologicamente_activa(self):
        """Devuelve True si la concentracion >= 0.05 ng/mL."""
        return self.concentracion >= 0.05

    # --- metodos accion ---

    def transcurrir_minutos(self, minutos):
        """Aplica decaimiento exponencial: C = C0 * 0.5^(t / t1/2)."""
        self.concentracion = self.concentracion * 0.5 ** (
            minutos / self.vida_media_min
        )

    def reportar(self):
        """Imprime concentracion y estado."""
        estado = "activa" if self.es_fisiologicamente_activa() else "inactiva"
        print(f"adrenalina: {self.concentracion:.3f} ng/mL, {estado}")


# --- prueba ---

if __name__ == "__main__":
    a = Adrenalina(2.0)
    a.reportar()                  # 2.000 activa
    a.transcurrir_minutos(2)
    a.reportar()                  # 1.000 activa
    a.transcurrir_minutos(2)
    a.reportar()                  # 0.500 activa
    a.transcurrir_minutos(10)
    a.reportar()                  # 0.016 inactiva
