class Vino():
    def init(self, anada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS):

        self.nombre = nombre
        self.anada = anada
        self.fechaActualizacion = fechaActualizacion
        self.imagenEtiqueta = imagenEtiqueta
        self.notaDeCataBodega = notaDeCataBodega
        self.precioARS = precioARS

    def toJSON(self):
        return {
            "nombre" : self.nombre,
            "anada" : self.anada,
            "fechaActualizacion" : self.fechaActualizacion,
            "imagenEtiqueta" : self.imagenEtiqueta,
            "notaDeCataBodega" : self.notaDeCataBodega,
            "precioARS" : self.precioARS
        }
