class Hemoglobina:
    def __init__(self,saturacion):
        self.nombre     =               "hemoglobina"
        self.saturacion =               saturacion      #protegido con encapsulacion @property
        self.moleculas_transportadas =  0

    @property
    #getter: un metdoo que permite acceder a un atributo en una clase determinada
    def saturacion(self):           #el metodo se llama igual que el atributo publico
        return self._saturacion     #guion bajo para no tocar directamente

    #setter: un metodo que permite establecer o modificar el valor de un atributo en una clase. 
    @saturacion.setter               # el decorador usa el nombre de arribe
    def saturacion(self, valor: float) -> None:
        if not isinstance(valor, (int,float)):
            raise TypeError("La saturacion debe ser un valor numerico sin %")
        elif 0 > valor:
            raise ValueError(f"La saturacion no puede ser menor a 0. Recibi {valor}")
        elif valor > 100:
            raise ValueError(f"La saturacion no puede ser mayor a 100%, recibi {valor}")
        self._saturacion = valor    # El setter guarda el valor

    # metodos
    def es_hipoxica(self):
        if self.saturacion < 90: 
            return True
        else:
            return False

    def respirar(self, porcentaje):
        self.saturacion = porcentaje + self.saturacion
        if self.saturacion > 100:
            self.saturacion = 100
        elif self.saturacion < 0:
            self.saturacion = 0

    def consumir_oxigeno(self, valor):
        self.saturacion = self.saturacion - valor
        if self.saturacion < 0:
            self.saturacion = 0
        elif self.saturacion >= 90:
            self.moleculas_transportadas
        elif self.saturacion < 90:
            # El cuerpo pide mas hemoglobina
            self.moleculas_transportadas = self.moleculas_transportadas + 1


    def reportar(self):
        estado = "hipoxica" if self.es_hipoxica() else "normal"
        print(f"Hb: {self.saturacion:.1f}%, {estado}, transportes extra: {self.moleculas_transportadas}")

hb = Hemoglobina(98.0)
hb.reportar()
hb.consumir_oxigeno(10)
hb.reportar()
hb.respirar(5)
hb.reportar()
hb.consumir_oxigeno(50)
hb.reportar()
hb.consumir_oxigeno(60)
hb.reportar()