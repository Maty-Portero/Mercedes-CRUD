import sqlite3
import os

# Verificar ambos archivos db2.db
db_paths = [
    r"g:\Mercedes-CRUD\MercedesCRUD\db2.db",
    r"g:\Mercedes-CRUD\db2.db"
]

for db_path in db_paths:
    if os.path.exists(db_path):
        print(f"\n{'='*60}")
        print(f"Base de datos: {db_path}")
        print(f"Tamaño: {os.path.getsize(db_path)} bytes")
        print('='*60)
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Obtener todas las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"{table_name}: {count} registros")
        
        conn.close()
    else:
        print(f"\n❌ No existe: {db_path}")
