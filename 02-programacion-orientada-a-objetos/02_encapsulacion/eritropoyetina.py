class Eritropoyetina:
    def __init__(self,concentracion_inicial):
        self.concentracion           = concentracion_inicial
        self.nombre                  = "Eritropoyetina"
        self.vida_media_horas        = 5.0
        self.eritrocitos_estimulados = 0  

    @property
    # getter: un metodo que permite acceder a un atribituo en una clase determinada 
    def concentracion(self): #el metdo se llama igual que el atributo publico 
        return self._concentracion #el guion bajo dice que no lo toque directo 

    # Setter: Un método que permite establecer o modificar el valor de un atributo en una clase.
    @concentracion.setter #el deocrador usa el nmbre de arriba. 
    def concentracion(self, valor: float) -> None: # agregar None el setter no devuelve nada solo guarda. 
        if not isinstance(valor, (int,float)):
            raise TypeError("concentracion debe ser numerico")
        if valor < 0:
            raise ValueError(f"la concentracion no puede ser negativa (recibi {valor})")
        self._concentracion = valor #el setter guarda el valor. 

    #Método pregunta → devuelve valor con `return`, no imprime
    def es_nivel_terapeutico(self):
        return self.concentracion >= 4.0
    #Método acción → modifica estado o imprime, no devuelve
    def transcurrir_horas(self,horas):
        self.concentracion = self.concentracion * 0.5 ** (horas/self.vida_media_horas)
    def estimular_eritropoyesis(self):
        if self.es_nivel_terapeutico():
            self.eritrocitos_estimulados = self.eritrocitos_estimulados+1
    def reportar(self):
        estado = "terapeutico" if self.es_nivel_terapeutico() else "subterapeutico"
        print(f"EPO: {self.concentracion:.2f} mU/mL, {estado}, eritrocitos estimulados: {self.eritrocitos_estimulados}")

epo = Eritropoyetina(10.0)
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

epo.concentracion = -5