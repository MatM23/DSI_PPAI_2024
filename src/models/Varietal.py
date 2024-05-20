class Varietal():

    def init(self, descripcion, porcentajeComposicion):
        self._descripcion = descripcion
        self._porcentajeComposicion = porcentajeComposicion

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "descripcion" : self.getDescripcion(),
            "porcentajeComposicion" : self.getPorcentajeComposicion()
        }

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