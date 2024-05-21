from flask import Blueprint, jsonify, request
# para importar los metodos de gestorimportaractbodega
from services import GestorImportarActBodega

gestor = GestorImportarActBodega.Gestor()

#Cada una de estas rutas debe ser importada en el app.py, y así
# poder utilizar estos 'planos'

main= Blueprint('bodega_blueprint', __name__)
@main.route('/')
def indice():
    return jsonify({'message':"HOLA"})


@main.route('/bodega/actualizables')
def importActVinosBodega(): # Funcion para obtener las bodegas que necesitan actualizarse
    bodegas = gestor.buscarBodegas()
    return jsonify(bodegas)

@main.route('/bodega/actualizables/<nombreBodega>/vinos')
def obtenerActualizacionesBodega(): # Funcion para obtener las actualizaciones de la bodega seleccionada
    nombreBodega = request.args.get('nombreBodega')
    vinos = GestorImportarActBodega.obtenerActualizacionesBodega(nombreBodega)
    return jsonify(vinos)