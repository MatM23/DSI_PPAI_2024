from datetime import datetime
import sqlite3

def inicializarBase():
    conexion = sqlite3.connect('ppai.db')  # Conexión a la base de datos en memoria
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM bodegas")
    cursor.execute("DELETE FROM vinos")

    # Crear las tablas en la base de datos en memoria
    cursor.execute('''CREATE TABLE IF NOT EXISTS bodegas (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          descripcion TEXT,
                          fechaUltimaActualizacion DATE,
                          periodoActualizacion INTEGER,
                          historia TEXT,
                          vinosNombres TEXT,
                          FOREIGN KEY (vinosNombres) REFERENCES vinos(nombre)
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS vinos (
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
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS maridaje (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          descripcion TEXT
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tipoUva (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          descripcion TEXT
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS varietal (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          descripcion TEXT,
                          porcentajeComposicion REAL,
                          tipoUvaNombre TEXT,
                          FOREIGN KEY(tipoUvaNombre) REFERENCES tipoUva(nombre)
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS enofilo (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          apellido TEXT,
                          imagenPerfil BLOB,
                          nombreSiguiendo TEXT,
                          nombreUsuario TEXT,
                          FOREIGN KEY(nombreSiguiendo) REFERENCES siguiendo(nombre),
                          FOREIGN KEY(nombreUsuario) REFERENCES siguiendo(nombre)
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT,
                          contraseña TEXT,
                          premium TEXT
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS siguiendo (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          tipoSiguiendo TEXT,
                          bodegaOEnofilo TEXT,
                          fechaInicio DATE,
                          fechaFin DATE,
                           
                           FOREIGN KEY (bodegaOEnofilo) REFERENCES bodegas(nombre),
                           FOREIGN KEY (bodegaOEnofilo) REFERENCES enofilo(nombre)
                      )''')
    
    
    # Insertar datos de ejemplo en la base de datos en memoria
    # BODEGAS
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaActualizacion, periodoActualizacion, historia, vinosNombres) VALUES (?, ?, ?, ?, ?, ?)",
                    ('Viñedos', 'Bodega familiar dedicada a la producción de vinos artesanales.', datetime(2024,5,19).date(), 60, 'Fundada en 1980 por la familia García, Los Viñedos ha sido reconocida por sus vinos de alta calidad.', 'GarnachaRosé,ChardonnayPremium'))
    
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaActualizacion, periodoActualizacion, historia, vinosNombres) VALUES (?, ?, ?, ?, ?, ?)", 
               ('Olivo', 'Bodega ecológica comprometida con la sostenibilidad y el medio ambiente.', datetime(2024,4,20).date(), 90, 'Inaugurada en 1995, El Olivo se destaca por su enfoque en la producción de vinos orgánicos.', 'MonastrellCasaCisca,GarnachaRosé,MerlotRobleViejo'))
    
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaActualizacion, periodoActualizacion, historia, vinosNombres) VALUES (?, ?, ?, ?, ?, ?)", 
               ('Montaña', 'Bodega boutique situada en las montañas, especializada en vinos de altura.', datetime(2023,3,10).date(), 90, 'Desde 2002, La Montaña ha cautivado a los amantes del vino con su singularidad y carácter.', 'MalbecdeAltura,SyrahReservaEspecial,MenciaCepasViejas'))
    
    cursor.execute("INSERT INTO bodegas (nombre, descripcion, fechaUltimaActualizacion, periodoActualizacion, historia, vinosNombres) VALUES (?, ?, ?, ?, ?, ?)", 
               ('Roble', 'Bodega tradicional con más de un siglo de historia en la elaboración de vinos tintos.', datetime(2024,2,5).date(), 30, 'Desde 1890, ha sido un referente en la producción de Malbec y Cabernet Sauvignon.', 'Trivento,SyrahReservaEspecial,MalbecdeAltura,MerlotRobleViejo'))
    

    # VINOS
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('Trivento', 2000, datetime(2024,12,16).date(), 'imagen.jpg', 2550, 8, 'Roble', 'Papas', 'Varietal 1'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('GarnachaRosé', 2002, datetime(2024,7,15).date(), 'imagen.jpg', 5000, 10,'Viñedos', 'Carne', 'Varietal 4'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('ChardonnayPremium', 1999, datetime(2024,5,14).date(), 'imagen.jpg', 1500, 4,'Olivo', 'Empanadas', 'Varietal 7'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('SyraReservaEspecial', 2010, datetime(2024,1,13).date(), 'imagen.jpg', 4500, 7,'Olivo', 'Pescado', 'Varietal 3'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('MerlotRobleViejo', 2010, datetime(2024,6,12).date(), 'imagen.jpg', 3500, 1,'Montaña', 'Pastas', 'Varietal 2'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('MenciaCepasViejas', 2009, datetime(2024,3,11).date(), 'imagen.jpg', 3000, 7,'Montaña', 'Carne', 'Varietal 5'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('MonastrellCasaCisca', 2014, datetime(2024,3,10).date(), 'imagen.jpg', 1000, 6,'Roble', 'Pescado', 'Varietal 6'))
    cursor.execute("INSERT INTO vinos (nombre, anada, fechaActualizacion, imagenEtiqueta, precioARS, notaDeCataBodega, bodegaNombre, maridajeNombre, varietalNombre) VALUES (?,?,?,?,?,?,?,?,?)",
                   ('MalbecdeAltura', 1998, datetime(2024,5,9).date(), 'imagen.jpg', 5000, 10,'Roble', 'Pastas', 'Varietal 1'))
    
    #MARIDAJES
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Papas','Viene bien con papas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Carne','Viene bien con carnes rojas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Empanadas','Viene bien con empanadas'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Pescado','Viene bien con pescado'))
    cursor.execute("INSERT INTO maridaje (nombre, descripcion) VALUES (?,?)",
                   ('Pastas','Viene bien con pastas'))
    

    # TIPOS DE UVA 
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Garnacha','Calidez y sedosidad en la boca'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Mencia','Aterciopelado y afrutado'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Monastrell','Color rubí intenso, aroma a frutas rojas y negras'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Merlot','Aroma a frutos rojos, junto con humo, guinda, trufas y cuero'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Malbec','Versátil, con cuerpo, afrutado y amaderado'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Syrah','Sabor intenso, con buen cuerpo y acidez equilibrada'))
    cursor.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?,?)",
                   ('Chardonnay','Cuerpo ligero, aroma a caramelo, miel y avellanas'))
    

    # VARIETAL
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('Varietal 1',87,'Malbec' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('Varietal 2',81,'Merlot' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('Varietal 3',87,'Syrah' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('Varietal 4',99,'Garnacha' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('Varietal 5',84,'Mencia' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('Varietal 6',89,'Monastrell' ))
    cursor.execute("INSERT INTO varietal (descripcion, porcentajeComposicion, tipoUvaNombre) VALUES (?,?,?)",
                   ('Varietal 7',90,'Chardonnay' ))
    

    

    # SIGUIENDO
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, bodegaOEnofilo, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Agustin','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, bodegaOEnofilo, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Bodega','BodegaCentral','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, bodegaOEnofilo, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Matias','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, bodegaOEnofilo, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Francisco','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, bodegaOEnofilo, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, bodegaOEnofilo, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Agustin','2024-5-19', datetime.now().date()))
    cursor.execute("INSERT INTO siguiendo (tipoSiguiendo, bodegaOEnofilo, fechaInicio, fechaFin) VALUES (?,?,?,?)",
                   ('Enofilo','Agostina','2024-5-19', datetime.now().date()))


    # ENOFILO
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias'))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Matias','Moreno','imagen.jpg', 'Agustin'))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Agostina'))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Francisco','Figueroa','imagen.jpg', 'BodegaCentral'))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias'))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias'))
    cursor.execute("INSERT INTO enofilo (nombre, apellido, imagenPerfil, nombreSiguiendo) VALUES (?,?,?,?)",
                   ('Agustin','Hillar','imagen.jpg', 'Matias'))


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

def getConexion():
    conn = sqlite3.connect('ppai.db') 
    return conn