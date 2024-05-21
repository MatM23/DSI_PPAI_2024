from models import Bodega
from models import Maridaje
from dateutil.relativedelta import *
from models import Varietal
from database.db_sqlite import getConexion

class Vino():
    def __init__(self, nombre, anada, fechaActualizacion, imagenEtiqueta, notaDeCataBodega, precioARS, bodega, maridaje, varietal):

        self._nombre = nombre
        self._anada = anada
        self._fechaActualizacion = fechaActualizacion
        self._imagenEtiqueta = imagenEtiqueta
        self._notaDeCataBodega = notaDeCataBodega
        self._precioARS = precioARS
        self._bodega = bodega
        self._maridaje = []
        self._varietal = []

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "anada" : self.getAnada(),
            "fechaActualizacion" : self.getFechaActualizacion(),
            "imagenEtiqueta" : self.getImagenEtiqueta(),
            "notaDeCataBodega" : self.getNotaDeCataBodega(),
            "precioARS" : self.getPrecioARS(),
            "maridaje" : self.getMaridaje(),
            "bodega" : self.getBodega(),
            "varietal" : self.getVarietal()
        }
    
    # Atributos propios de VINO
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

    # funcion para saber si el vino es de una bodega enviada por parametro
    def esDeBodega(self, nombreDeBodegaABuscar): 
        conn = getConexion()
        cursor = conn.cursor()
        stringBodega = self.getBodega()
    
        filaBaseDatosBodega= cursor.execute("SELECT nombre, descripcion, historia, fechaUltimaActualizacion, periodoActualizacion, vinosNombres FROM bodegas WHERE nombre=?", (stringBodega,)).fetchone()
        bodega = Bodega.Bodega(filaBaseDatosBodega[0], filaBaseDatosBodega[1], filaBaseDatosBodega[2], filaBaseDatosBodega[3], filaBaseDatosBodega[4], filaBaseDatosBodega[5])
        conn.close()
        if nombreDeBodegaABuscar == bodega.getNombre():
            
            return True
        return False

    # funcion para saber si el vino debe actualizarse, comparando fecha actual y fecha actualizacion
    def esActualizable(self, fechaActual):
        fechaActualizacion = self.getFechaActualizacion()
        if fechaActual > fechaActualizacion:
            return True
        return False
    
    # Relaciones con otras clases
    # Relacion con Bodega
    def setBodega(self, bodega):
        self._bodega = bodega

    def getBodega(self):
        return self._bodega
    
    # Relacion con maridaje
    def getNombreMaridaje(self, nombre):
        for maridaje in self._maridaje:
            if maridaje.getNombre() == nombre:
                return maridaje
        return None 
        

    def setMaridaje(self, maridaje):
        if not isinstance(maridaje, Maridaje):
            raise TypeError("maridaje debe ser una instancia de la clase Maridaje")
        self._maridaje.append(maridaje)

    def getMaridaje(self):
        return self._maridaje
    
    # Relacion con Varietal
    def setVarietal(self, varietal):
        if not isinstance(varietal, Varietal):
            raise TypeError("varietal debe ser una instancia de la clase Varietal")
        self._varietal.append(varietal)

    def getVarietal(self):
        return self._varietal

    def getNombreVarietal(self, nombre):
        for varietal in self._varietal:
            if varietal.getNombre() == nombre:
                return varietal
        return None
    
    def new(anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, maridaje, varietal):
       vino = Vino()
       vino.init(anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, maridaje, varietal)
       return vino

    def crearVarietal(descripcion, porcentajeComposicion):
        varietal = Varietal.new(descripcion, porcentajeComposicion)
        return varietal


