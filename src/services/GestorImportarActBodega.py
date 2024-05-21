from models import Bodega
from datetime import datetime
from database import db_sqlite
from models import Maridaje
from models import TipoUva
from models import Enofilo
from models import Siguiendo
from models import Vino
import sqlite3


class Gestor:
    conexion = sqlite3.connect(':memory:')  # Conexión a la base de datos en memoria
    cursor = conexion.cursor()
    bodegas = []  # Atributo de clase para almacenar todas las bodegas

    @classmethod 
    def agregarBodega(cls, bodega):
        if not isinstance(bodega, Bodega):
            raise TypeError("Debe ser una instancia de la clase Bodega")
        cls.bodegas.append(bodega)

    def getFechaActual():
        fechaActual = datetime.now
        return fechaActual

    @classmethod
    def buscarBodegas(self):
        bodegasActualizar = []
        cursor.execute("SELECT * FROM Bodega")
        bodegasTodas = cursor.fetchall()
        fechaActual = self.getFechaActual()
        for bodega in bodegasTodas:
            if bodega.esParaActualizar(fechaActual):
                bodegasActualizar.append(bodega.getNombre())
                ## ¿bodegaParaActualizar=Bodega(fila[0], fila[1], fila[2], fila[3])?
        return bodegasActualizar
    
    def definirVinosAActualizar(self, nombreBodega, vinos):
        bodega = cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
        vinosActualizar = []
        for vino in vinos:
            if bodega.tieneVino(nombreBodega):
                vinosActualizar.append(vino)
        return vinosActualizar
    
    # funcion para obtener actualizaciones de bodega usando la base de datos
    def obtenerActualizacionesBodega(self, nombreBodega):
        bodega = cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
        return bodega.getVinos() #tenemos q definir que vinos y de donde vienen 
    
    # funcion para actualizar fecha de actualizacion de la bodega seleccionada
    def actualizarFechaActualizacionBodega(self, nombreBodega):
        fechaActual = datetime.now()
        bodega = cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
        bodega.setFechaUltimaActualizacion(fechaActual)
        
    def buscarMaridaje(maridaje):
        maridajeBuscado = Maridaje.sosMaridaje(maridaje)
        return maridajeBuscado
    
    # funcion para buscar tipo de uva usando el metodo esElTipoUva de la clase TipoUva
    def buscarTipoUva(tipoUva):
        tipoUvaBuscado = TipoUva.esElTipoUva(tipoUva)
        return tipoUvaBuscado
    
    def actualizarVino(self, vinos):
        for vino in vinos:
            Bodega.actualizarVino(vino)

    # Funcion para buscar seguidores de la bodega seleccionada
    def buscarSeguidoresBodega(self, nombreBodega):
        seguidores = []
        enofilos = cursor.execute("SELECT * FROM Siguiendo WHERE tipoSiguiendo = Enofilo",)
        for enofilo in enofilos:
            if enofilo.sosSeguidorBodega(nombreBodega):
                seguidores.getNombre().append()
    
    def crearVino(anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, maridaje, varietal):
        vino = Vino.new(anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, maridaje, varietal)
        return vino