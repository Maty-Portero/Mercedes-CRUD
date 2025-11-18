import sqlite3
import os

# Ruta a la base de datos (en el directorio raíz de MercedesCRUD)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "db2.db")

print(f"Creando/Actualizando base de datos: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear todas las tablas basadas en los JSON disponibles

# Tabla RRHH
cursor.execute("""
CREATE TABLE IF NOT EXISTS RRHH (
    ID_RRHH INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Empleado INTEGER,
    Tipo_Evento TEXT,
    Fecha TEXT,
    Descripcion TEXT
)
""")

# Tabla VENTAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS VENTAS (
    ID_Venta INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Cliente INTEGER,
    Fecha TEXT,
    Total REAL,
    Estado TEXT
)
""")

# Tabla COMPRAS  
cursor.execute("""
CREATE TABLE IF NOT EXISTS COMPRAS (
    ID_Compra INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Proveedor INTEGER,
    Fecha TEXT,
    Total REAL,
    Estado TEXT
)
""")

# Tabla LOGISTICA
cursor.execute("""
CREATE TABLE IF NOT EXISTS LOGISTICA (
    ID_Logistica INTEGER PRIMARY KEY AUTOINCREMENT,
    Tipo TEXT,
    Origen TEXT,
    Destino TEXT,
    Estado TEXT,
    Fecha TEXT
)
""")

# Tabla PRODUCCION_TAREAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCCION_TAREAS (
    ID_Tarea INTEGER PRIMARY KEY AUTOINCREMENT,
    Descripcion TEXT,
    Responsable TEXT,
    Estado TEXT,
    Fecha_Inicio TEXT,
    Fecha_Fin TEXT
)
""")

# Tabla MANTENIMIENTO_EQUIPOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS MANTENIMIENTO_EQUIPOS (
    ID_Equipo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Tipo TEXT,
    Estado TEXT,
    Ultima_Revision TEXT
)
""")

# Tabla MARKETING
cursor.execute("""
CREATE TABLE IF NOT EXISTS MARKETING (
    ID_Campana INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Tipo TEXT,
    Estado TEXT,
    Presupuesto REAL,
    Fecha_Inicio TEXT,
    Fecha_Fin TEXT
)
""")

# Mantener las tablas existentes que ya están en uso
cursor.execute("""
CREATE TABLE IF NOT EXISTS CAMPANAS_MARKETING (
    ID_Campana INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Tipo TEXT,
    Estado TEXT,
    Fecha_Inicio TEXT,
    Fecha_Fin TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS VENTAS_PEDIDOS (
    ID_Pedidos INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Cliente INTEGER,
    ID_Usuario_Vendedor INTEGER,
    Estado_Pedido TEXT,
    Monto_Total REAL
)
""")

conn.commit()
conn.close()

print("Base de datos creada exitosamente con todas las tablas.")
