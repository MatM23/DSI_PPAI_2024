from flask import Flask
from config import config
from flask_cors import CORS
from database.db_sqlite import inicializarBase
from database.dbvinos import inicializarBaseVinos
app = Flask(__name__)
CORS(app)


# Rutas a importar
from routes import PantallaImportadorActBodega

# @app.route("/bodegas/<nombreBodega>/vinos")
# def obtenerVinosBodega(nombreBodega):


if __name__ == "__main__":
    app.config.from_object(config['development'])
    inicializarBase()
    inicializarBaseVinos()
    # Blueprints / planos
    app.register_blueprint(PantallaImportadorActBodega.main, url_prefix='/api')

    app.run()
