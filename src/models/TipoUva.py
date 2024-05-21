class TipoUva():

    def __init__(self, descripcion, nombre):
        self._nombre = nombre
        self._descripcion = descripcion

    def toJSON(self):
        return {
            "nombreTipoUva" : self.getNombre(),
            "descripcion" : self.getDescripcion()
        }
    
    def esElTipoUva(self, tipo):
        return self.getNombre() == tipo

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
