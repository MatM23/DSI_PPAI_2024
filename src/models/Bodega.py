
from dateutil.relativedelta import *
from models import Vino
from datetime import datetime, date, timedelta
from database.db_sqlite import getConexion

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
    def tieneVino(self, nombreVino): 
    
        conn = getConexion()
        cursor = conn.cursor()
        filaBaseDatosVino= cursor.execute("SELECT nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre FROM vinos WHERE nombre=?", (str(nombreVino),)).fetchone()
        print('gfdhsfhd',filaBaseDatosVino)
        if filaBaseDatosVino is not None:
            vino = Vino.Vino(filaBaseDatosVino[0], filaBaseDatosVino[1], filaBaseDatosVino[2], filaBaseDatosVino[3], filaBaseDatosVino[4], filaBaseDatosVino[5], filaBaseDatosVino[6], filaBaseDatosVino[7], filaBaseDatosVino[8])
            print('Vino encontrado:', vino)     
        else:
            print('No se encontró ningún vino con el nombre proporcionado')
        #if vino.esDeBodega(self.getNombre()):
        #   return True
        #return False

    def actualizarVino(self, vino):
        fechaActual = datetime.now()
        if vino.esActualizable(fechaActual):
            vino.setFechaActualizacion(vino.getFechaActualizacion())
            vino.setImagenEtiqueta(vino.getImagenEtiqueta())
            vino.setNotaDeCataBodega(vino.getNotaDeCataBodega())
            vino.setPrecioARS(vino.getPrecioARS())
    
