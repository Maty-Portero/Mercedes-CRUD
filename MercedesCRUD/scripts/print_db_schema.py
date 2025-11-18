import sqlite3

DB_PATH = "../database.db"  # Ajusta el path si es necesario

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
