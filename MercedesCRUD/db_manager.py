from PySide6.QtSql import QSqlDatabase, QSqlQuery

_db = None

def get_db_connection(db_name="database.db"):
    """Establece y devuelve la conexión a la base de datos."""
    global _db
    
    if _db and _db.isOpen():
        return _db
    
    _db = QSqlDatabase.database()
    if not _db.isValid():
        _db = QSqlDatabase.addDatabase("QSQLITE")
        
    _db.setDatabaseName(db_name)
    if not _db.open():
        print(f"ERROR: No se pudo abrir la base de datos: {_db.lastError().text()}")
        return None
        
    print("Conexión a la DB establecida.")
    return _db

def execute_query(sql_query, params=None):
    """Función de utilidad para ejecutar consultas con parámetros opcionales."""
    db = get_db_connection()
    if not db:
        return None
        
    query = QSqlQuery(db)
    
    if params:
        # Usar prepared statement con placeholders (?)
        if not query.prepare(sql_query):
            print(f"Error preparando consulta: {query.lastError().text()}")
            return None
        
        # Agregar los parámetros
        for param in params:
            query.addBindValue(param)
        
        if not query.exec():
            print(f"Error en consulta: {query.lastError().text()}")
            return None
    else:
        # Sin parámetros, ejecutar directamente
        if not query.exec(sql_query):
            print(f"Error en consulta: {query.lastError().text()}")
            return None
        
    return query