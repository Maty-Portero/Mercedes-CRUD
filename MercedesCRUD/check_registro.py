import sqlite3

conn = sqlite3.connect('db2.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM E_MOVILIDAD_REGISTRO ORDER BY ID_Cambios DESC LIMIT 10')
print('Registros en E_MOVILIDAD_REGISTRO:')
for row in cursor.fetchall():
    print(row)
conn.close()
