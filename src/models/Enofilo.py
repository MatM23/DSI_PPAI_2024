class Enofilo():

    def init(self, nombre, apellido, imagenPerfil):
        self._nombre = nombre
        self._apellido = apellido
        self._imagenPerfil = imagenPerfil
    
    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "apellido" : self.getApellido(),
            "imagenPerfil" : self.getImagenPerfil(),
        }
    
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