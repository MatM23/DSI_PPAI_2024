class Usuario():

    def init(self, nombre, contrasena, premium):
        self._nombre = nombre
        self._contrasena = contrasena
        self._premium = premium

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "contrasena" : self.getContrasena(),
            "premium" : self.getPremium(),
        }

    def getNombre(self):
        return self._nombre

    def setNombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena")
        self._nombre = valor

    def getContrasena(self):
        return self._contrasena

    def setContrasena(self, valor):
        self._contrasena = valor

    def getPremium(self):
        return self._premium

    def setPremium(self, valor):
        self._premium = valor
