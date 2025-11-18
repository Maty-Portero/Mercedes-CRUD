"""
Script para implementar funciones CRUD en todos los sectores.
Ejecuta este script para generar las implementaciones completas.
"""

# Configuración de cada sector
SECTORES = {
    "main_ventas.py": {
        "tabla": "VENTAS_PEDIDOS",
        "id_col": "ID_Pedidos",
        "headers": ["ID_Pedidos", "ID_Cliente", "ID_Usuario_Vendedor", "Estado_Pedido", "Monto_Total"],
        "columnas_insert": ["ID_Cliente", "ID_Usuario_Vendedor", "Estado_Pedido", "Monto_Total"],
        "tipos": ["int", "int", "str", "float"],
        "labels": ["ID Cliente:", "ID Usuario Vendedor:", "Estado Pedido:", "Monto Total:"],
        "nombre_entidad": "venta",
        "prefix": "venta"
    },
    "main_compras.py": {
        "tabla": "ORDENES_COMPRA",
        "id_col": "ID_OC",
        "headers": ["ID_OC", "ID_Proveedor", "Estado", "ID_Usuario_Aprobador", "ID_Usuario_Solicitante", "Monto_Total"],
        "columnas_insert": ["ID_Proveedor", "Estado", "ID_Usuario_Aprobador", "ID_Usuario_Solicitante", "Monto_Total"],
        "tipos": ["int", "str", "int", "int", "float"],
        "labels": ["ID Proveedor:", "Estado:", "ID Usuario Aprobador:", "ID Usuario Solicitante:", "Monto Total:"],
        "nombre_entidad": "orden de compra",
        "prefix": "compra"
    },
    "main_logistica.py": {
        "tabla": "SEGUIMIENTO_LOGISTICO",
        "id_col": "ID_Seguimiento",
        "headers": ["ID_Seguimiento", "Tipo_Logistica", "Origen", "Destino", "Estado_Actual", "ID_Pedido_OC"],
        "columnas_insert": ["Tipo_Logistica", "Origen", "Destino", "Estado_Actual", "ID_Pedido_OC"],
        "tipos": ["str", "str", "str", "str", "int"],
        "labels": ["Tipo Logística:", "Origen:", "Destino:", "Estado Actual:", "ID Pedido/OC:"],
        "nombre_entidad": "seguimiento",
        "prefix": "pedido"
    },
    "main_produccion_tareas.py": {
        "tabla": "ORDENES_PRODUCCION",
        "id_col": "ID_Orden",
        "headers": ["ID_Orden", "ID_Producto", "Cantidad_A_Producir", "Estado"],
        "columnas_insert": ["ID_Producto", "Cantidad_A_Producir", "Estado"],
        "tipos": ["int", "int", "str"],
        "labels": ["ID Producto:", "Cantidad a Producir:", "Estado:"],
        "nombre_entidad": "orden de producción",
        "prefix": "equipo"
    },
    "main_mantenimiento.py": {
        "tabla": "INVENTARIO",
        "id_col": "ID_Inventario",
        "headers": ["ID_Inventario", "ID_Producto", "Cantidad_Stock"],
        "columnas_insert": ["ID_Producto", "Cantidad_Stock"],
        "tipos": ["int", "int"],
        "labels": ["ID Producto:", "Cantidad Stock:"],
        "nombre_entidad": "item de inventario",
        "prefix": "equipo"
    }
}

def generate_agregar_function(config):
    """Genera la función agregar para un sector."""
    campos_input = []
    campos_add_row = []
    valores_array = []
    
    for i, (label, tipo, col) in enumerate(zip(config["labels"], config["tipos"], config["columnas_insert"])):
        var_name = f"input_{i}"
        campos_input.append(f"        {var_name} = QLineEdit()")
        campos_add_row.append(f'        layout.addRow("{label}", {var_name})')
        
        if tipo == "int":
            valores_array.append(f"int({var_name}.text())")
        elif tipo == "float":
            valores_array.append(f"float({var_name}.text())")
        else:
            valores_array.append(f"{var_name}.text()")
    
    columnas_str = '", "'.join(config["columnas_insert"])
    valores_str = ",\n                    ".join(valores_array)
    
    return f'''    @Slot()
    def agregar_{config["prefix"]}(self):
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        import db_manager
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar {config["nombre_entidad"].title()}")
        layout = QFormLayout()
        
{chr(10).join(campos_input)}
        
{chr(10).join(campos_add_row)}
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["{columnas_str}"]
                values = [
                    {valores_str}
                ]
                
                if db_manager.insert_record("{config["tabla"]}", columns, values):
                    QMessageBox.information(self, "Éxito", "{config["nombre_entidad"].title()} agregado correctamente.")
                    self.load_sector_data("{config["tabla"]}", {config["headers"]}, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo agregar {config["nombre_entidad"]}.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {{e}}")'''

print("Implementaciones CRUD generadas. Copie y pegue las funciones en los archivos correspondientes.")
print("\nEjemplo para Ventas:")
print(generate_agregar_function(SECTORES["main_ventas.py"]))
