from bodega import Bodega
from maridaje import Maridaje

class Vino():
    def init(self, anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, maridaje):

        self._nombre = nombre
        self._anada = anada
        self._fechaActualizacion = fechaActualizacion
        self._imagenEtiqueta = imagenEtiqueta
        self._notaDeCataBodega = notaDeCataBodega
        self._precioARS = precioARS
        self._bodega = bodega
        self._maridaje = []

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "anada" : self.getAnada(),
            "fechaActualizacion" : self.getFechaActualizacion(),
            "imagenEtiqueta" : self.getImagenEtiqueta(),
            "notaDeCataBodega" : self.getNotaDeCataBodega(),
            "precioARS" : self.getPrecioARS(),
            "maridaje" : self.getMaridaje(),
            "bodega" : self.getBodega()
        }

    def getPrecioARS(self):
        return self._precioARS

    def setPrecioARS(self, valor):
        self._precioARS = valor

    def getNotaDeCataBodega(self):
        return self._notaDeCataBodega

    def setNotaDeCataBodega(self, valor):
        self._notaDeCataBodega = valor

    def getImagenEtiqueta(self):
        return self._imagenEtiqueta

    def setImagenEtiqueta(self, valor):
        self._imagenEtiqueta = valor

    def getFechaActualizacion(self):
        return self._fechaActualizacion

    def setFechaActualizacion(self, valor):
        self._fechaActualizacion = valor

    def getAnada(self):
        return self._anada

    def setAnada(self, valor):
        self._anada = valor

    def getNombre(self):
        return self._nombre

    def setNombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena")
        self._nombre = valor
    
    def getNombreBodega(self):
        return self._bodega.getNombre()

    def setBodega(self, bodega):
        if not isinstance(bodega, Bodega):
            raise TypeError("bodega debe ser una instancia de la clase Bodega")
        self._bodega = bodega
    
    def getBodega(self):
        return self._bodega

    def getNombreMaridaje(self):
        return self._maridaje.getNombre()

    def setMaridaje(self, maridaje):
        if not isinstance(maridaje, Maridaje):
            raise TypeError("maridaje debe ser una instancia de la clase Maridaje")
        self._maridaje.append(maridaje)
    
    def getMaridaje(self):
        return self._maridaje



