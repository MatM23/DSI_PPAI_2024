from datetime import datetime
import sqlite3

def inicializarBaseVinos():
    conexion = sqlite3.connect('vinos.db')  # Conexión a la base de datos en memoria
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM vinos")

    cursor.execute('''CREATE TABLE IF NOT EXISTS vinos  (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          anada INTEGER,
                          fechaActualizacion DATE,
                          imagenEtiqueta TEXT,
                          precioARS REAL,
                          notaDeCataBodega INTEGER,
                          bodegaNombre TEXT,
                          maridajeNombre TEXT,
                          varietalNombre TEXT,
                          FOREIGN KEY (bodegaNombre) REFERENCES bodegas(nombre),
                          FOREIGN KEY (maridajeNombre) REFERENCES maridaje(nombre),
                          FOREIGN KEY (varietalNombre) REFERENCES varietal(nombre)
                      )''')
    

    # VINOS
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('Trivento Reserva', 2000, datetime(2024,12,16).date(), 'imagen.jpg', 7000, 8, 'Roble', 'Papas', 'Varietal 1'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('Garnacha Rosé', 2002, datetime(2024,7,15).date(), 'imagen.jpg', 10000, 10,'Viñedos', 'Carne', 'Varietal 4'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('Vino Landi', 1999, datetime(2024,5,14).date(), 'imagen.jpg', 1500, 4,'Roble', 'Empanadas', 'Varietal 7'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('Syrah Reserva Especial', 2010, datetime(2024,1,13).date(), 'imagen.jpg', 4500, 7,'Olivo', 'Pescado', 'Varietal 3'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('Vino Figueroa', 2010, datetime(2024,6,12).date(), 'imagen.jpg', 3500, 1,'Montaña', 'Pastas', 'Varietal 2'))

    conexion.commit()
    conexion.close()

def getConexionVinos():
    conn = sqlite3.connect('vinos.db') 
    return conn
    
