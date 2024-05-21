from models import TipoUva

class Varietal(): #FALTA RELACIONARLO CON TIPOUVA, VER METODO GETTIPOUVA

    def init(self, descripcion, porcentajeComposicion):
        self._descripcion = descripcion
        self._porcentajeComposicion = porcentajeComposicion

    def toJSON(self):
        return {
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

    # Relacion con TipoUva
    def getTipoUva(self):
        return self._tipoUva
    
    def setTipoUva(self, valor):
        if not isinstance(valor, TipoUva):
            raise ValueError("El tipo de uva debe ser una instancia de la clase Tipo Uva")
        self._tipoUva = valor

    def getNombreTipoUva(self):
        return self._tipoUva.getNombre()
    
    # Ver! Ya hay un método constructor arriba llamado "Init"
    def new(descripcion, porcentajeComposicion):
       varietal = Varietal()
       varietal.init(descripcion, porcentajeComposicion)
       return varietal