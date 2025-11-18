import sqlite3
import os

# Ruta a la base de datos
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "db2.db")

print(f"Poblando base de datos: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Datos para tabla RRHH
rrhh_data = [
    (1, "Contratación", "2024-01-15", "Nuevo empleado en área de producción"),
    (2, "Evaluación", "2024-02-20", "Evaluación trimestral de desempeño"),
    (3, "Capacitación", "2024-03-10", "Curso de seguridad industrial"),
    (4, "Promoción", "2024-04-05", "Ascenso a supervisor de área"),
    (5, "Licencia", "2024-05-18", "Licencia médica por 15 días"),
    (1, "Amonestación", "2024-06-22", "Incumplimiento de horario"),
    (3, "Bonus", "2024-07-30", "Bono por cumplimiento de objetivos"),
]

cursor.executemany("""
    INSERT INTO RRHH (ID_Empleado, Tipo_Evento, Fecha, Descripcion)
    VALUES (?, ?, ?, ?)
""", rrhh_data)

# Datos para tabla VENTAS
ventas_data = [
    (101, "2024-01-10", 125000.50, "Pendiente"),
    (102, "2024-01-15", 89500.00, "Aprobado"),
    (103, "2024-02-05", 234000.75, "Aprobado"),
    (101, "2024-02-20", 67800.00, "Cancelado"),
    (104, "2024-03-12", 456000.00, "Aprobado"),
    (102, "2024-03-28", 198500.25, "Pendiente"),
    (105, "2024-04-08", 321000.00, "Aprobado"),
]

cursor.executemany("""
    INSERT INTO VENTAS (ID_Cliente, Fecha, Total, Estado)
    VALUES (?, ?, ?, ?)
""", ventas_data)

# Datos para tabla COMPRAS
compras_data = [
    (201, "2024-01-08", 45000.00, "Entregado"),
    (202, "2024-01-22", 78500.50, "En Tránsito"),
    (203, "2024-02-14", 123000.00, "Entregado"),
    (201, "2024-03-05", 56700.25, "Pendiente"),
    (204, "2024-03-19", 234000.00, "Entregado"),
    (202, "2024-04-10", 98400.75, "En Tránsito"),
    (205, "2024-04-25", 187000.00, "Pendiente"),
]

cursor.executemany("""
    INSERT INTO COMPRAS (ID_Proveedor, Fecha, Total, Estado)
    VALUES (?, ?, ?, ?)
""", compras_data)

# Datos para tabla LOGISTICA
logistica_data = [
    ("Nacional", "Buenos Aires", "Córdoba", "En Tránsito", "2024-01-12"),
    ("Internacional", "Hamburgo", "Buenos Aires", "Aduana", "2024-01-18"),
    ("Nacional", "Mendoza", "Rosario", "Entregado", "2024-02-03"),
    ("Nacional", "Córdoba", "Tucumán", "En Preparación", "2024-02-15"),
    ("Internacional", "Shanghái", "Buenos Aires", "En Tránsito", "2024-03-01"),
    ("Nacional", "Buenos Aires", "Mar del Plata", "Entregado", "2024-03-20"),
    ("Internacional", "Miami", "Buenos Aires", "En Preparación", "2024-04-05"),
]

cursor.executemany("""
    INSERT INTO LOGISTICA (Tipo, Origen, Destino, Estado, Fecha)
    VALUES (?, ?, ?, ?, ?)
""", logistica_data)

# Datos para tabla PRODUCCION_TAREAS
produccion_data = [
    ("Ensamblaje de motor clase A", "Juan Pérez", "Completado", "2024-01-05", "2024-01-18"),
    ("Control de calidad lote 234", "María García", "En Proceso", "2024-02-01", "2024-02-15"),
    ("Pintura carrocerías", "Carlos López", "Completado", "2024-02-10", "2024-02-24"),
    ("Instalación sistema eléctrico", "Ana Martínez", "En Proceso", "2024-03-01", "2024-03-20"),
    ("Pruebas de rendimiento", "Diego Rodríguez", "Pendiente", "2024-03-15", None),
    ("Ensamblaje interior vehículo", "Laura Fernández", "En Proceso", "2024-04-01", "2024-04-15"),
    ("Revisión final lote 456", "Roberto Sánchez", "Pendiente", "2024-04-10", None),
]

cursor.executemany("""
    INSERT INTO PRODUCCION_TAREAS (Descripcion, Responsable, Estado, Fecha_Inicio, Fecha_Fin)
    VALUES (?, ?, ?, ?, ?)
""", produccion_data)

# Datos para tabla MANTENIMIENTO_EQUIPOS
mantenimiento_data = [
    ("Prensa Hidráulica #1", "Prensa", "Operativo", "2024-03-15"),
    ("Robot Soldador A-23", "Robot", "En Mantenimiento", "2024-01-20"),
    ("Línea de Montaje 3", "Línea", "Operativo", "2024-04-01"),
    ("Compresor Industrial", "Compresor", "Operativo", "2024-02-10"),
    ("Puente Grúa 5 Ton", "Grúa", "Fuera de Servicio", "2023-12-05"),
    ("Horno de Pintura", "Horno", "Operativo", "2024-03-28"),
    ("Torno CNC-450", "Torno", "En Mantenimiento", "2024-02-15"),
]

cursor.executemany("""
    INSERT INTO MANTENIMIENTO_EQUIPOS (Nombre, Tipo, Estado, Ultima_Revision)
    VALUES (?, ?, ?, ?)
""", mantenimiento_data)

# Datos para tabla MARKETING
marketing_data = [
    ("Lanzamiento EQS 2024", "Lanzamiento", "Activa", 250000.00, "2024-01-10", "2024-03-31"),
    ("Test Drive Premium", "Evento", "Completada", 120000.00, "2024-02-01", "2024-02-28"),
    ("Campaña Digital Verano", "Digital", "Activa", 180000.00, "2024-03-01", "2024-05-31"),
    ("Sponsoreo F1 Argentina", "Sponsoreo", "Planificada", 500000.00, "2024-06-01", "2024-06-30"),
    ("Newsletter Clientes VIP", "Email Marketing", "Activa", 45000.00, "2024-01-15", "2024-12-31"),
    ("Feria Auto Show BA", "Evento", "Planificada", 320000.00, "2024-07-10", "2024-07-15"),
    ("Campaña Clase C", "Publicidad", "Completada", 275000.00, "2023-11-01", "2024-01-31"),
]

cursor.executemany("""
    INSERT INTO MARKETING (Nombre, Tipo, Estado, Presupuesto, Fecha_Inicio, Fecha_Fin)
    VALUES (?, ?, ?, ?, ?, ?)
""", marketing_data)

conn.commit()
print("✓ Datos agregados exitosamente")
print(f"  - RRHH: {len(rrhh_data)} registros")
print(f"  - VENTAS: {len(ventas_data)} registros")
print(f"  - COMPRAS: {len(compras_data)} registros")
print(f"  - LOGISTICA: {len(logistica_data)} registros")
print(f"  - PRODUCCION_TAREAS: {len(produccion_data)} registros")
print(f"  - MANTENIMIENTO_EQUIPOS: {len(mantenimiento_data)} registros")
print(f"  - MARKETING: {len(marketing_data)} registros")

conn.close()
