from models import Bodega
from models import Enofilo

class Siguiendo():

    def init(self, fechaFin, fechaInicio, bodegaOEnofilo, tipoSiguiendo):

        self._fechaFin = fechaFin
        self._fechaInicio = fechaInicio
        self._bodegaOEnofilo = bodegaOEnofilo
        self._tipoSiguiendo = tipoSiguiendo

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

    # ¿? =================
    
    def getNombre(self):
            return self._bodegaOEnofilo.getNombre()
    
    def setNombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena")
        self._nombre = valor 
    
    # ====================

    def getTipo(self):
        return self._tipoSiguiendo

    def setTipo(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El tipo debe ser una cadena")      
        self._tipoSiguiendo = valor

    def sosDeBodega(self, nombreBodega):
        if (self._getTipo() == 'Bodega') and (nombreBodega == self._getNombre()):
            return True