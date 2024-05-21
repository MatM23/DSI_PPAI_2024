from models.Bodega import Bodega
from datetime import datetime, date
from database.db_sqlite import inicializarBase, getConexion
from database.dbvinos import inicializarBaseVinos, getConexionVinos
from models import Maridaje
from models import TipoUva
from models import Enofilo
from models import Siguiendo
from models.Vino import Vino
import sqlite3
from flask import jsonify

class Gestor():
    actualizaciones = []
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
    
    def obtenerActualizacionesBodega(self, bodegaNombre):
        conexion = getConexionVinos()

        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, anada, fechaActualizacion, imagenEtiqueta, notaDeCataBodega, precioARS, bodegaNombre, maridajeNombre, varietalNombre FROM vinos WHERE bodegaNombre=?", (str(bodegaNombre),))
        filasBaseDatosVinos = cursor.fetchall()
 
        for fila in filasBaseDatosVinos:
            vino = Vino(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8])
            self.actualizaciones.append(vino)
        
        conexion.close()
        return self.definirVinosAActualizar(bodegaNombre)
        

    def definirVinosAActualizar(self, bodegaNombre):
        conn = getConexion()
        cursor = conn.cursor()
        filaBaseDeDatosBodega = cursor.execute("SELECT nombre, descripcion, historia, fechaUltimaActualizacion, periodoActualizacion, vinosNombres FROM bodegas WHERE nombre = ?", (bodegaNombre,)).fetchone()
        bodega = Bodega(filaBaseDeDatosBodega[0], filaBaseDeDatosBodega[1], filaBaseDeDatosBodega[2], filaBaseDeDatosBodega[3], filaBaseDeDatosBodega[4], filaBaseDeDatosBodega[5])
        vinosActualizar = []
        for vino in self.actualizaciones:
            if bodega.tieneVino(vino.getNombre()) == True:
                vinosActualizar.append(vino)
        
        conn.close()
        return vinosActualizar
    
    # funcion para obtener actualizaciones de bodega usando la base de datos
    #def obtenerActualizacionesBodega(self, nombreBodega):
     #   cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
      #  bodega = cursor.fetchone()
       # return bodega.getVinos() #tenemos q definir que vinos y de donde vienen 
    

    # funcion para actualizar fecha de actualizacion de la bodega seleccionada
    #def actualizarFechaActualizacionBodega(self, nombreBodega):
     #   fechaActual = datetime.now()
      #  cursor.execute("SELECT * FROM Bodega WHERE nombre = ?", (nombreBodega,))
       # bodega = cursor.fetchone()
        #bodega.setFechaUltimaActualizacion(fechaActual)
        
    
    #def buscarMaridaje(maridaje):
     #   maridajeBuscado = Maridaje.sosMaridaje(maridaje)
      #  return maridajeBuscado
    
    # funcion para buscar tipo de uva usando el metodo esElTipoUva de la clase TipoUva
   # def buscarTipoUva(tipoUva):
    #    tipoUvaBuscado = TipoUva.esElTipoUva(tipoUva)
     #   return tipoUvaBuscado
    
#    def actualizarVino(self, vinos):
 #       for vino in vinos:
  #          Bodega.actualizarVino(vino)


    # Funcion para buscar seguidores de la bodega seleccionada
    #def buscarSeguidoresBodega(self, nombreBodega):
     #   seguidores = []
      #  enofilos = cursor.execute("SELECT * FROM Siguiendo WHERE tipoSiguiendo = Enofilo",)
       # for enofilo in enofilos:
        #    if enofilo.sosSeguidorBodega(nombreBodega):
         #       seguidores.getNombre().append()

    
    #def crearVino(anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, maridaje, varietal):
     #   vino = Vino.new(anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, maridaje, varietal)
      #  return vino
