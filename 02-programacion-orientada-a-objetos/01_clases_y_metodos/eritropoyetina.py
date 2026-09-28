"""
La eritropoyetina (EPO) 
hormona producida por el riñón que estimula la producción de glóbulos rojos.
"""

#Clase → gen (el molde)
class Eritropoyetina:
    #`__init__` → plegamiento inicial, guarda atributos
    def __init__(self,concentracion_inicial):
        #`self` → "esta molécula específica"
        self._validar(concentracion_inicial)
        self.nombre = "eritropoyetina"
        self.concentracion = concentracion_inicial
        self.vida_media_horas = 5.0
        self.eritrocitos_estimulados = 0

    #`@staticmethod` + `_validar` → guardián de tipos y rangos
    @staticmethod
    def _validar(concentracion_inicial):
        if not isinstance(concentracion_inicial, (int,float)):
            raise TypeError("concentracion inicial debe ser numerico")
        if concentracion_inicial < 0:
            raise ValueError(
                f"la concentracion no puede ser negativa (recibi {concentracion_inicial})"
            )
    #Método pregunta → devuelve valor con `return`, no imprime
    def es_nivel_terapeutico(self):
        return self.concentracion >= 4.0
    #Método acción → modifica estado o imprime, no devuelve
    def transcurrir_horas(self,horas):
        self.concentracion = self.concentracion * 0.5 ** (horas/self.vida_media_horas)
    def estimular_eritropoyesis(self, ):
        if self.es_nivel_terapeutico():
            self.eritrocitos_estimulados = self.eritrocitos_estimulados+1
    def reportar(self):
        estado = "terapeutico" if self.es_nivel_terapeutico() else "subterapeutico"
        print(f"EPO: {self.concentracion:.2f} mU/mL, {estado}, eritrocitos estimulados: {self.eritrocitos_estimulados}")



epo = Eritropoyetina(20.0)
epo.reportar()
epo.estimular_eritropoyesis()
epo.reportar()

epo.transcurrir_horas(10)
epo.reportar()
epo.estimular_eritropoyesis()
epo.reportar()

epo.transcurrir_horas(5)
epo.reportar()
epo.estimular_eritropoyesis()
epo.reportar()