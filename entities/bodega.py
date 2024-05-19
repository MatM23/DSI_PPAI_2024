class Bodega():
    def init(self, nombre, descripcion, historia, fechaUltimaActualizacion, periodoActualizacion):

        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaUltimaActualizacion = fechaUltimaActualizacion
        self.periodoActualizacion = periodoActualizacion
        self.historia = historia

    def toJSON(self):
        return {
            "nombre" : self.nombre,
            "descripcion" : self.descripcion,
            "fechaUltimaActualizacion" : self.fechaUltimaActualizacion,
            "historia" : self.historia,
            "periodoActualizacion" : self.periodoActualizacion
        }