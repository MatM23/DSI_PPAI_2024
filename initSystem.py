from services import gestorImportarActBodega
from datetime import datetime

# Lista de datos de bodegas (nombre, ubicacion)
datos_bodegas = [
    ("Bodega Central", "Ciudad A", "ABC", datetime(2024, 5, 19), 3),
    ("Bodega Central", "Ciudad B", "ABC", datetime(2024, 5, 10), 4),
    ("Bodega Central", "Ciudad C", "ABC", datetime(2024, 3, 20), 5),
    ("Bodega Central", "Ciudad D", "ABC", datetime(2024, 2, 4), 10),
    ("Bodega Central", "Ciudad E", "ABC", datetime(2021, 7, 19), 8),
    ("Bodega Central", "Ciudad F", "ABC", datetime(2024, 1, 8), 3),
    ("Bodega Central", "Ciudad G", "ABC", datetime(2024, 2, 28), 3),
    ("Bodega Central", "Ciudad H", "ABC", datetime(2023, 9, 19), 5),
    ("Bodega Central", "Ciudad I", "ABC", datetime(2024, 1, 6), 3),
    ("Bodega Central", "Ciudad J", "ABC", datetime(2024, 4, 28), 2),
    ("Bodega Central", "Ciudad K", "ABC", datetime(2024, 5, 10), 3),
    ("Bodega Central", "Ciudad L", "ABC", datetime(2024, 5, 11), 3),
    ("Bodega Central", "Ciudad M", "ABC", datetime(2024, 5, 12), 7),
    ("Bodega Central", "Ciudad N", "ABC", datetime(2024, 1, 29), 3),
    ("Bodega Central", "Ciudad O", "ABC", datetime(2024, 2, 23), 3),
    ("Bodega Central", "Ciudad P", "ABC", datetime(2024, 3, 19), 6),
    ("Bodega Central", "Ciudad Q", "ABC", datetime(2024, 4, 19), 3),
    ("Bodega Central", "Ciudad R", "ABC", datetime(2024, 5, 19), 4),
    ("Bodega Central", "Ciudad S", "ABC", datetime(2024, 1, 19), 3),
    ("Bodega Central", "Ciudad T", "ABC", datetime(2024, 2, 19), 2),
    ("Bodega Central", "Ciudad U", "ABC", datetime(2024, 3, 19), 3),
    ("Bodega Central", "Ciudad V", "ABC", datetime(2024, 4, 19), 2),
    ("Bodega Central", "Ciudad W", "ABC", datetime(2024, 5, 19), 3),
    ("Bodega Central", "Ciudad X", "ABC", datetime(2024, 5, 19), 2),
]


# Agregar todas las bodegas a la vez
for bodega in datos_bodegas:
    gestorImportarActBodega.bodegas.append(bodega)
