from flask import Blueprint, jsonify

# Modelos
from services import GestorImportarActBodega

#Cada una de estas rutas debe ser importada en el app.py, y así
# poder utilizar estos 'planos'

main= Blueprint('bodega_blueprint', __name__)
@main.route('/')
def obtenerBodegas():
    bodegas=GestorImportarActBodega.buscarBodegas()
    return jsonify(bodegas)