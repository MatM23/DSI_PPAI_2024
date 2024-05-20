from entities import bodega
from datetime import datetime

class gestorImportarActBodega():
    bodegas = []
    bodegaElegida = None
    enofilosSeguidores = None
    vinosImportados = None
    maridaje = None
    tipoUva = None

    def buscarBodegas(self):
        fechaActual = datetime.now()
        esParaActualizar = bodega.esParaActualizar(fechaActual)

