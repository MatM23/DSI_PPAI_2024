from services import GestorImportarActBodega
from datetime import datetime
import sqlite3


def inicializarBase():
    conexion = sqlite3.connect(':memory:')  # Conexión a la base de datos en memoria
    cursor = conexion.cursor()

    # Crear las tablas en la base de datos en memoria
    cursor.execute('''CREATE TABLE bodegas (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          descripcion TEXT,
                          fechaUltimaActualizacion DATE,
                          periodoActualizacion INTEGER,
                          historia TEXT
                      )''')
    cursor.execute('''CREATE TABLE vinos (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          anada INTEGER,
                          fechaActualizacion DATE,
                          imagenEtiqueta TEXT,
                          precioARS REAL,
                          notaDeCataBodega INTEGER
                          bodegaNombre TEXT,
                          maridajeNombre TEXT
                          varietalNombre TEXT
                          FOREIGN KEY (bodegaNombre) REFERENCES bodegas(nombre)
                          FOREIGN KEY (maridajeNombre) REFERENCES maridaje(nombre)
                          FOREIGN KEY (varietalNombre) REFERENCES varietal(nombre)
                      )''')
    
    cursor.execute('''CREATE TABLE maridaje (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          descripcion TEXT
                      )''')
    
    cursor.execute('''CREATE TABLE tipoUva (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          descripcion TEXT
                      )''')
    
    cursor.execute('''CREATE TABLE varietal (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          descripcion TEXT,
                          porcentajeComposicion REAL
                          tipoUvaNombre TEXT
                          FOREIGN KEY(tipoUvaNombre) REFERENCES tipoUva(nombre)
                      )''')
    
    cursor.execute('''CREATE TABLE enofilo (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          apellido TEXT,
                          imagenPerfil BLOB
                          nombreSiguiendo TEXT
                          nombreUsuario TEXT
                          FOREIGN KEY(nombreSiguiendo) REFERENCES siguiendo(nombre)
                          FOREIGN KEY(nombreUsuario) REFERENCES siguiendo(nombre)
                      )''')
    
    cursor.execute('''CREATE TABLE usuario (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT
                          contraseña TEXT
                          premium TEXT
                      )''')
    
    cursor.execute('''CREATE TABLE siguiendo (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          tipoSiguiendo TEXT
                          nombre TEXT
                          fechaInicio DATE
                          fechaFin DATE
                           FOREIGN KEY (nombre) REFERENCES bodegas(nombre)
                           FOREIGN KEY (nombre) REFERENCES enofilo(nombre)
                      )''')
    
    
    # Insertar datos de ejemplo en la base de datos en memoria
    # BODEGAS
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 3, 19).date(), 4, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 2, 19).date(), 4, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 1, 19).date(), 4, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 5, 19).date(), 6, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2023, 7, 19).date(), 8, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 1, 25).date(), 4, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 5, 1).date(), 1, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 3, 3).date(), 4, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 5, 19).date(), 2, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 5, 19).date(), 3, 'hola'))
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaAztualizacion, periodoActualizacion, historia) VALUES (?, ?, ?, ?, ?)", 
               ('BodegaCentral', 'oishfs', datetime(2024, 5, 19).date(), 5, 'hola'))


    # VINOS
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,16).date(), 'imagen.jpg', 255, 8, 'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,15).date(), 'imagen.jpg', 50, 10,'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,14).date(), 'imagen.jpg', 150, 4,'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,13).date(), 'imagen.jpg', 450, 7,'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,12).date(), 'imagen.jpg', 350, 1,'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,11).date(), 'imagen.jpg', 300, 7,'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,10).date(), 'imagen.jpg', 100, 6,'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,9).date(), 'imagen.jpg', 500, 10,'BodegaCentral', 'Papas', 'Malbec'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?)",
                   ('Vino tinto', 2024, datetime(2024,15,8).date(), 'imagen.jpg', 400, 4,'BodegaCentral', 'Papas', 'Malbec'))
    
    
    #MARIDAJES
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Papas','Viene bien con papas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Carne','Viene bien con carne'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Empanadas','Viene bien con empanadas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Cereales','Viene bien con cereales'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Galletas','Viene bien con galletas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Palitos','Viene bien con palitos'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Milanesas','Viene bien con milanesas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Bifes','Viene bien con bifes'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Papas','Viene bien con papas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Pan','Viene bien con pan'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Papas','Viene bien con papas'))
    

    # TIPOS DE UVA 
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Garnacha','Agrio'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Mencia','Dulce'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Mostranell','Feo'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Merlot','Rico'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Malbec','Horrible'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Syrah','Caro'))
    

    # VARIETAL
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('dsjiosdj',87,'Malbec' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('dsjiosdj',81,'Merlot' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('dsjiosdj',87,'Syrah' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('dsjiosdj',99,'Garnacha' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('dsjiosdj',84,'Mencia' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('dsjiosdj',89,'Mostranell' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('dsjiosdj',87,'Malbec' ))
    

    # SIGUIENDO
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, nombre, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Agustin','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, nombre, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Bodega','BodegaCentral','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, nombre, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Matias','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, nombre, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Francisco','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, nombre, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, nombre, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Agustin','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, nombre, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Agostina','2024-5-19', datetime.now().date()))


    # ENOFILO
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias', 'Enofilo'  ))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Matias','Moreno','imagen.jpg', 'Agustin', 'Enofilo'  ))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Agostina', 'Enofilo'  ))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Francisco','Figueroa','imagen.jpg', 'BodegaCentral', 'Bodega'  ))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias', 'Enofilo'  ))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias', 'Enofilo'  ))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias', 'Enofilo'  ))


    # USUARIO
    cursor.execute("INSERT INTO usuario (nombre, contraseña, premium) VALUES (?,?,?)",
                   ('Agustinhola', 'skfksv', 'NO'  ))
    cursor.execute("INSERT INTO usuario (nombre, contraseña, premium) VALUES (?,?,?)",
                   ('Franciscohola', 'skfksv', 'SI'  ))
    cursor.execute("INSERT INTO usuario (nombre, contraseña, premium) VALUES (?,?,?)",
                   ('Matiashola', 'skfksv', 'NO'  ))
    cursor.execute("INSERT INTO usuario (nombre, contraseña, premium) VALUES (?,?,?)",
                   ('Agostinahola', 'skfksv', 'SI'  ))           


    conexion.commit()
    conexion.close()
