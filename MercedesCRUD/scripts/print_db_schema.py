import sqlite3
import os

# Usar la misma ruta relativa que create_db2_schema.py
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "db2.db")

def print_db_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Tablas en la base de datos:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        print(f"\nTabla: {table_name}")
        cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  - {col[1]} ({col[2]})")
    conn.close()

if __name__ == "__main__":
    print_db_schema(DB_PATH)
    
    # Guardar en archivo
    import sys
    original_stdout = sys.stdout
    with open("g:/Mercedes-CRUD/MercedesCRUD/reports/db_schema.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        print_db_schema(DB_PATH)
    sys.stdout = original_stdout
    print("\nEsquema guardado en reports/db_schema.txt")
