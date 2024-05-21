from models import Siguiendo
from models import Usuario
from models import Vino


class Enofilo():
    def __init__(self, nombre, apellido, imagenPerfil, siguiendo, usuario, vino):

        self._nombre = nombre
        self._apellido = apellido
        self._imagenPerfil = imagenPerfil
        self._siguiendo = []
        self._usuario = usuario
        self._vino = []

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "apellido" : self.getApellido(),
            "imagenPerfil" : self.getImagenPerfil(),
            "siguiendo" : self.getSiguiendo(),
            "usuario" : self.getUsuario(),
            "vino" : self.getVino()
        }


    # Atributos propios de enofilo
    def getNombre(self):
        return self._nombre

    def setNombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena")
        self._nombre = valor

    def getApellido(self):
        return self._apellido

    def setApellido(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El apellido debe ser una cadena")
        self._apellido = valor

    def getImagenPerfil(self):
        return self._imagenPerfil

    def setImagenPerfil(self, valor):
        self._imagenPerfil = valor

    # Relaciones con las otras clases
    # Relacion con siguiendo 
    def getNombreSiguiendo(self, nombre):
        for siguiendo in self._siguiendo:
            if siguiendo.getNombre() == nombre:
                return siguiendo
        return None

    def setSiguiendo(self, siguiendo):
        if not isinstance(siguiendo, Siguiendo):
            raise TypeError("siguiendo debe ser una instancia de la clase Siguiendo")
        self._siguiendo.append(siguiendo)

    def getSiguiendo(self):
        return self._siguiendo

    # Relacion con Usuario
    def getNombreUsuario(self):
        return self._usuario.getNombre()

    def setUsuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("usuario debe ser una instancia de la clase Usuario")
        self._usuario = usuario

    def getUsuario(self):
        return self._usuario

    # Relacion con Vino
    def getNombreVino(self, nombre):
        for vino in self._vino:
            if vino.getNombre() == nombre:
                return vino
        return None

    def setVino(self, vino):
        if not isinstance(vino, Vino):
            raise TypeError("vino debe ser una instancia de la clase Vino")
        self._vino.append(vino)

    def getVino(self):
        return self._vino
    
    def sosSeguidorBodega(self, nombreBodega):
        for seguidor in self._siguiendo:
            if seguidor.sosDeBodega(nombreBodega):
                return True

