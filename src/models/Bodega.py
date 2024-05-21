
from dateutil.relativedelta import *
from models import Vino
from datetime import datetime, date, timedelta

class Bodega():
    def __init__(self, nombre, descripcion, historia, fechaUltimaActualizacion, periodoActualizacion, vinos):

        self._nombre = nombre
        self._descripcion = descripcion
        self._fechaUltimaActualizacion = fechaUltimaActualizacion
        self._periodoActualizacion = periodoActualizacion
        self._historia = historia
        self._vinos = vinos

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "descripcion" : self.getDescripcion(),
            "fechaUltimaActualizacion" : self.getFechaUltimaActualizacion(),
            "historia" : self.getHistoria(),
            "periodoActualizacion" : self.getPeriodoActualizacion(),
            "vinos" : self.getVinos()
        }

    def getNombre(self):
        return self._nombre

    def setNombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena")
        self._nombre = valor

    def getDescripcion(self):
        return self._descripcion

    def setDescripcion(self, valor):
        if not isinstance(valor, str):
            raise ValueError("La descripcion debe ser una cadena")
        self._descripcion = valor

    def getFechaUltimaActualizacion(self):
        return self._fechaUltimaActualizacion

    def setFechaUltimaActualizacion(self, valor):
        self._fechaUltimaActualizacion = valor

    def getPeriodoActualizacion(self):
        return self._periodoActualizacion

    def setPeriodoActualizacion(self, valor):
        self._periodoActualizacion = valor

    def getHistoria(self):
        return self._historia

    def setHistoria(self, valor):
        self._historia = valor

    def esParaActualizar(self, fechaActual): 
        if fechaActual > ((datetime.strptime(self.getFechaUltimaActualizacion(), "%Y-%m-%d").date()) + timedelta(days=int(self.getPeriodoActualizacion()))):
            return True
        return False
    
    # Relacion con Vino siendo este una coleccion
    def getVinos(self):
        return self._vinos
    
    def setVinos(self, vino):
        if not isinstance(vino, Vino):
            raise TypeError("El vino debe ser una instancia de la clase Vino")
        self._vinos.append(vino)

    def getNombreVino(self, nombre):
        for vino in self._vinos:
            if vino.getNombre() == nombre:
                return vino
        return None 
    
    
    # funcion para saber si la bodega tiene un vino utilizando la funcion esDeBodega de la clase Vino
    def tieneVino(self, nombre): 
        for vino in self._vinos:
            if vino.esDeBodega(nombre):
                return True
        return False

    def actualizarVino(self, vino):
        fechaActual = datetime.now()
        if vino.esActualizable(fechaActual):
            vino.setFechaActualizacion(vino.getFechaActualizacion())
            vino.setImagenEtiqueta(vino.getImagenEtiqueta())
            vino.setNotaDeCataBodega(vino.getNotaDeCataBodega())
            vino.setPrecioARS(vino.getPrecioARS())
    
