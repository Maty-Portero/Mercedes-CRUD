import sqlite3
import os

# Ruta a la base de datos
db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "database.db")

# Datos de prueba para logística
logistica_data = [
    ("Nacional", "Buenos Aires", "Córdoba", "En_Tránsito", 801),
    ("Internacional", "Madrid", "Buenos Aires", "Pendiente", 802),
    ("Nacional", "Rosario", "Mendoza", "Entregado", 601),
    ("Nacional", "Buenos Aires", "Tucumán", "En_Tránsito", 602),
    ("Internacional", "São Paulo", "Buenos Aires", "En_Tránsito", 801),
    ("Nacional", "Córdoba", "Salta", "Pendiente", 602),
    ("Nacional", "Buenos Aires", "Mar del Plata", "Entregado", 601),
    ("Internacional", "Santiago", "Buenos Aires", "En_Tránsito", 802),
    ("Nacional", "Mendoza", "Buenos Aires", "Entregado", 601),
    ("Internacional", "Lima", "Buenos Aires", "Pendiente", 802),
    ("Nacional", "La Plata", "Neuquén", "En_Tránsito", 601),
    ("Internacional", "Montevideo", "Buenos Aires", "Entregado", 801),
    ("Nacional", "Buenos Aires", "Bariloche", "Pendiente", 602),
    ("Nacional", "Salta", "Jujuy", "En_Tránsito", 601),
    ("Internacional", "Bogotá", "Buenos Aires", "En_Tránsito", 802),
    ("Nacional", "Córdoba", "Buenos Aires", "Entregado", 601),
    ("Nacional", "Tucumán", "Mendoza", "Pendiente", 602),
    ("Internacional", "Rio de Janeiro", "Buenos Aires", "En_Tránsito", 801),
    ("Nacional", "Buenos Aires", "Ushuaia", "Pendiente", 602),
    ("Nacional", "Mendoza", "San Juan", "Entregado", 601)
]

print(f"Conectando a base de datos: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Agregando 20 registros a SEGUIMIENTO_LOGISTICO...")
exitosos = 0
for data in logistica_data:
    try:
        cursor.execute(
            "INSERT INTO SEGUIMIENTO_LOGISTICO (Tipo_Logistica, Origen, Destino, Estado_Actual, ID_Pedido_OC) VALUES (?, ?, ?, ?, ?)",
            data
        )
        exitosos += 1
    except Exception as e:
        print(f"Error al insertar {data}: {e}")

conn.commit()
conn.close()

print(f"\n{exitosos} registros agregados exitosamente.")
