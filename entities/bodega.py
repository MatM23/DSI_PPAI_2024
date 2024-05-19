class Bodega():
    def init(self, nombre, descripcion, historia, fechaUltimaActualizacion, periodoActualizacion):

        self._nombre = nombre
        self._descripcion = descripcion
        self._fechaUltimaActualizacion = fechaUltimaActualizacion
        self._periodoActualizacion = periodoActualizacion
        self._historia = historia

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "descripcion" : self.getDescripcion(),
            "fechaUltimaActualizacion" : self.getFechaUltimaActualizacion(),
            "historia" : self.getHistoria(),
            "periodoActualizacion" : self.getPeriodoActualizacion()
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