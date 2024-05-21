from flask import Flask
from config import config
from database.db_sqlite import inicializarBase
app = Flask(__name__)

# Rutas a importar
from routes import PantallaImportadorActBodega

# @app.route("/bodegas/<nombreBodega>/vinos")
# def obtenerVinosBodega(nombreBodega):


if __name__ == "__main__":
    app.config.from_object(config['development'])
    inicializarBase()
    # Blueprints / planos
    app.register_blueprint(PantallaImportadorActBodega.main, url_prefix='/api/bodega')

    app.run()
