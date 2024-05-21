
class Maridaje():

    def init(self, nombre, descripcion):
        self._nombre = nombre
        self._descripcion = descripcion

    def toJSON(self):
        return {
            "nombre" : self.getNombre(),
            "descripcion" : self.getDescripcion(),
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
        
    def sosMaridaje(self, nombre):
        return self.getNombre() == nombre
