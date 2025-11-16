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

def fetch_all_data(sql_query, params=None):
    """
    Ejecuta una consulta SELECT y retorna los resultados como una lista de listas (filas).
    """
    query = execute_query(sql_query, params)
    
    if query is None:
        # Error al ejecutar o preparar la consulta.
        return None
        
    results = []
    
    # Recorrer los resultados de QSqlQuery
    while query.next():
        row = []
        # QSqlQuery no tiene un método directo para obtener todas las columnas de una vez.
        # Recorremos los índices de columna (desde 0 hasta el número total de columnas - 1)
        for i in range(query.record().count()):
            # .value(i) obtiene el valor de la columna en el índice i
            row.append(query.value(i))
        results.append(row)
        
    return results

def get_data_for_sector(table_name, columns):
    """
    Función generalizada para obtener datos de una tabla específica.
    :param table_name: Nombre de la tabla de la BD (ej: "SEGUIMIENTO_LOGISTICO").
    :param columns: Lista de nombres de las columnas a seleccionar.
    :return: Lista de listas con los datos.
    """
    columns_str = ", ".join(columns)
    
    # IMPORTANTE: Activar Foreign Keys si no se hace al abrir la conexión (solo para QSQLITE)
    execute_query("PRAGMA foreign_keys = ON;")
    
    query = f"SELECT {columns_str} FROM {table_name};"
    return fetch_all_data(query)