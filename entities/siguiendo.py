class Siguiendo():
    def init(self, fechaFin, fechaInicio):

        self._fechaFin = fechaFin
        self._fechaInicio = fechaInicio

    def toJSON(self):
        return {
            "fechaInicio" : self.getFechaInicio(),
            "fechaFin" : self.getFechaFin()
        }
    
    def getFechaInicio(self):
        return self._fechaInicio

    def setFechaInicio(self, valor):
        self._fechaInicio = valor
    
    def getFechaFin(self):
        return self._fechaFin

    def setFechaFin(self, valor):
        self._fechaFin = valor