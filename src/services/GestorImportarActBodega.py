from models.Bodega import Bodega
from datetime import datetime, date
from database.db_sqlite import inicializarBase, getConexion
from models import Maridaje
from models import TipoUva
from models import Enofilo
from models import Siguiendo
from models import Vino
import sqlite3

class Gestor():
    bodegas = []  # Atributo de clase para almacenar todas las bodegas

    @classmethod 
    def agregarBodega(cls, bodega):
        if not isinstance(bodega, Bodega):
            raise TypeError("Debe ser una instancia de la clase Bodega")
        cls.bodegas.append(bodega)

    def getFechaActual(self):
        fechaActual = date.today()
        return fechaActual

    
    def buscarBodegas(self):
        bodegasActualizar = []
        fechaActual = self.getFechaActual()

        conn = getConexion()
        
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, descripcion, historia, fechaUltimaActualizacion, periodoActualizacion, vinosNombres FROM bodegas")
        filasBaseDatos = cursor.fetchall()
        
        for fila in filasBaseDatos:
            bodega = Bodega(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])

            if bodega.esParaActualizar(fechaActual):
                    bodegasActualizar.append(bodega.getNombre())

        conn.close()
        return bodegasActualizar
    
    
    
    

    def definirVinosAActualizar(self, nombreBodega, vinos):
        cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
        bodega = cursor.fetchone()
        vinosActualizar = []
        for vino in vinos:
            if bodega.tieneVino(nombreBodega):
                vinosActualizar.append(vino)
        return vinosActualizar
    
    # funcion para obtener actualizaciones de bodega usando la base de datos
    def obtenerActualizacionesBodega(self, nombreBodega):
        cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
        bodega = cursor.fetchone()
        return bodega.getVinos() #tenemos q definir que vinos y de donde vienen 
    

    # funcion para actualizar fecha de actualizacion de la bodega seleccionada
    def actualizarFechaActualizacionBodega(self, nombreBodega):
        fechaActual = datetime.now()
        cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
        bodega = cursor.fetchone()
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
