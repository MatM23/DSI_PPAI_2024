class Varietal():
    def init(self, nombre, descripcion, porcentajeComposicion):

        self._nombre = nombre
        self._descripcion = descripcion
        self._porcentajeComposicion = porcentajeComposicion

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "descripcion" : self.getDescripcion(),
            "porcentajeComposicion" : self.getPorcentajeComposicion()
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
    
    def getPorcentajeComposicion(self):
        return self._porcentajeComposicion

    def setPorcentajeComposicion(self, valor):
        self._porcentajeComposicion = valor
