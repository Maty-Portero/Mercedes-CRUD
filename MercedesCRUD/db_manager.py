from PySide6.QtSql import QSqlDatabase, QSqlQuery
import os

_db = None

def get_db_connection(db_name=None):
    """Establece y devuelve la conexión a la base de datos."""
    global _db
    
    if _db and _db.isOpen():
        return _db
    
    # Si no se proporciona nombre, usar ruta absoluta al db2.db correcto
    if db_name is None:
        # Obtener el directorio donde está este archivo (db_manager.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_name = os.path.join(current_dir, "db2.db")
    
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

def insert_record(table_name, columns, values):
    """
    Inserta un nuevo registro en la tabla especificada.
    :param table_name: Nombre de la tabla
    :param columns: Lista de nombres de columnas
    :param values: Lista de valores correspondientes
    :return: True si fue exitoso, False si hubo error
    """
    placeholders = ", ".join(["?" for _ in values])
    columns_str = ", ".join(columns)
    query_str = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    
    result = execute_query(query_str, values)
    return result is not None

def update_record(table_name, columns, values, id_column, id_value):
    """
    Actualiza un registro existente en la tabla.
    :param table_name: Nombre de la tabla
    :param columns: Lista de nombres de columnas a actualizar
    :param values: Lista de valores correspondientes
    :param id_column: Nombre de la columna ID (ej: "ID_Empleado")
    :param id_value: Valor del ID del registro a actualizar
    :return: True si fue exitoso, False si hubo error
    """
    set_clause = ", ".join([f"{col} = ?" for col in columns])
    query_str = f"UPDATE {table_name} SET {set_clause} WHERE {id_column} = ?"
    
    params = list(values) + [id_value]
    result = execute_query(query_str, params)
    return result is not None

def delete_record(table_name, id_column, id_value):
    """
    Elimina un registro de la tabla.
    :param table_name: Nombre de la tabla
    :param id_column: Nombre de la columna ID
    :param id_value: Valor del ID del registro a eliminar
    :return: True si fue exitoso, False si hubo error
    """
    query_str = f"DELETE FROM {table_name} WHERE {id_column} = ?"
    result = execute_query(query_str, [id_value])
    return result is not None