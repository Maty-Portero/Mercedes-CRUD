import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtGui import QIcon
from ui_logistica import Ui_Widget
from image_loader import load_pixmap
import db_manager

# La clase MyWidget es tu vista de RRHH
class LogisticaWidget(QWidget):
    # Señal para notificar al manager que el usuario quiere cerrar sesión
    logout_requested = Signal()
    CEO=Signal(str)
    # Asumo que tienes un QLabel para mostrar el saludo de bienvenida en tu UI
    # Si no lo tienes, puedes agregarlo en el diseñador de Qt.

    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.label_5.setPixmap(load_pixmap("logo.png"))
        self.ui.label_5.setScaledContents(True)
        self.ui.label_7.setPixmap(load_pixmap("perfil-de-usuario.png"))
        self.ui.label_7.setScaledContents(True)
        icon_edit = QIcon(load_pixmap("edit.png"))
        self.ui.botonEditar1.setIcon(icon_edit)
        icon_close = QIcon(load_pixmap("close.png"))
        self.ui.botonSacar1.setIcon(icon_close)
        self.ui.botonAgregar.setIcon(QIcon(load_pixmap("c.png")))
        self.ui.botonOrdenar1.setIcon(QIcon(load_pixmap("down_arrow.png")))

        # Conexión de botones
        self.ui.botonAgregar.clicked.connect(self.agregar_pedido)
        self.ui.botonEditar1.clicked.connect(self.editar_pedido)
        self.ui.botonSacar1.clicked.connect(self.eliminar_pedido)
        self.ui.botonBuscar.clicked.connect(self.buscar_pedido)
        self.ui.botonOrdenar1.clicked.connect(self.ordenar_pedido)
        self.ui.botonAdmin.clicked.connect(self.admin_view)
        self.ui.botonLogOut.clicked.connect(self.Logout_requested)

        TABLE_NAME = "LOGISTICA"
        HEADERS = ["ID_Logistica", "Tipo", "Origen", "Destino", "Estado", "Fecha"]
        UI_TABLE = self.ui.tableWidget # reemplazado QLabel por QTableWidget en ui_logistica
        
        # Llamada para cargar los datos
        self.load_sector_data(TABLE_NAME, HEADERS, UI_TABLE)
    
    def load_sector_data(self, table_name, headers, table_widget):
        """
        Función reutilizable para cargar datos en la QTableWidget del sector.
        Utiliza el módulo db_manager para obtener los datos.
        """
        
        # 1. Obtener los datos usando la función del manager
        try:
            # Llamamos a la función generalizada en el módulo db_manager
            data = db_manager.get_data_for_sector(table_name, headers)
            
            if data is None:
                 QMessageBox.critical(self, "Error de BD", f"La consulta a la tabla '{table_name}' falló o no devolvió datos.")
                 return
                 
        except Exception as e:
            QMessageBox.critical(self, "Error de BD", f"Error al cargar datos de {table_name}: {e}")
            return

        # 2. Configurar la QTableWidget
        if not hasattr(table_widget, 'setColumnCount'):
            # El UI actual no contiene un QTableWidget en `UI_TABLE` (es un QLabel u otro widget).
            # Evitamos el crash y notificamos para que el diseñador UI sea corregido.
            print(f"[WARN] El widget proporcionado para mostrar la tabla ('{table_name}') no es una QTableWidget. Saltando carga.")
            return

        table_widget.setColumnCount(len(headers))
        # Mostrar los nombres de las columnas en la cabecera de la tabla
        table_widget.setHorizontalHeaderLabels(headers) 
        
        table_widget.setRowCount(0) 
        table_widget.setRowCount(len(data)) 

        # 3. Poblar la tabla
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                cell_item = QTableWidgetItem(str(item))
                cell_item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, cell_item)
        
        # 4. Estilo y configuración de tamaños
        # Distribuir columnas uniformemente en el espacio disponible
        header = table_widget.horizontalHeader()
        header.setStretchLastSection(False)
        
        # Hacer que todas las columnas se distribuyan equitativamente
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Aumentar altura de filas para mejor legibilidad
        table_widget.verticalHeader().setDefaultSectionSize(40)
        
        # Aumentar altura del header
        table_widget.horizontalHeader().setMinimumHeight(40)
        
        # Estilo CSS para mejorar la apariencia
        table_widget.setStyleSheet("""
            QTableWidget {

            }
            QHeaderView::section {
                background-color: #002d6b;
                color: white;
                padding: 5px;
                border: 1px solid #002d6b;
                font-weight: bold;
                font-size: 20px;
            }
            QTableCornerButton::section {
                background-color: #002d6b;
            }
            QTableWidget::item {
                border: 1px solid #e0e0e0;
                padding: 5px;
            }
        """)
        
        print(f"Sector {table_name}: {len(data)} registros cargados.")
        
        # Actualizar contador de registros
        if hasattr(self.ui, 'label_14'):
            self.ui.label_14.setText(f"Pedidos: {len(data)}")
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        self.current_user = username
        print(f"Usuario {username} ha ingresado a Logistica.") # Impresión de prueba

        

    @Slot()
    def agregar_pedido(self):
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        import db_manager
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Registro Logístico")
        layout = QFormLayout()
        
        tipo_input = QLineEdit()
        origen_input = QLineEdit()
        destino_input = QLineEdit()
        estado_input = QLineEdit()
        fecha_input = QLineEdit()
        
        layout.addRow("Tipo:", tipo_input)
        layout.addRow("Origen:", origen_input)
        layout.addRow("Destino:", destino_input)
        layout.addRow("Estado:", estado_input)
        layout.addRow("Fecha (YYYY-MM-DD):", fecha_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["Tipo", "Origen", "Destino", "Estado", "Fecha"]
                values = [
                    tipo_input.text(),
                    origen_input.text(),
                    destino_input.text(),
                    estado_input.text(),
                    fecha_input.text()
                ]
                
                if db_manager.insert_record("LOGISTICA", columns, values):
                    QMessageBox.information(self, "Éxito", "Registro logístico agregado correctamente.")
                    TABLE_NAME = "LOGISTICA"
                    HEADERS = ["ID_Logistica", "Tipo", "Origen", "Destino", "Estado", "Fecha"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo agregar el registro.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def editar_pedido(self):
        import db_manager
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un registro para editar.")
            return
        
        row = selected_rows[0].row()
        id_logistica = self.ui.tableWidget.item(row, 0).text()
        tipo_actual = self.ui.tableWidget.item(row, 1).text()
        origen_actual = self.ui.tableWidget.item(row, 2).text()
        destino_actual = self.ui.tableWidget.item(row, 3).text()
        estado_actual = self.ui.tableWidget.item(row, 4).text()
        fecha_actual = self.ui.tableWidget.item(row, 5).text()
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Editar Registro Logístico")
        layout = QFormLayout()
        
        tipo_input = QLineEdit(tipo_actual)
        origen_input = QLineEdit(origen_actual)
        destino_input = QLineEdit(destino_actual)
        estado_input = QLineEdit(estado_actual)
        fecha_input = QLineEdit(fecha_actual)
        
        layout.addRow("Tipo:", tipo_input)
        layout.addRow("Origen:", origen_input)
        layout.addRow("Destino:", destino_input)
        layout.addRow("Estado:", estado_input)
        layout.addRow("Fecha (YYYY-MM-DD):", fecha_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["Tipo", "Origen", "Destino", "Estado", "Fecha"]
                values = [
                    tipo_input.text(),
                    origen_input.text(),
                    destino_input.text(),
                    estado_input.text(),
                    fecha_input.text()
                ]
                
                if db_manager.update_record("LOGISTICA", columns, values, "ID_Logistica", int(id_logistica)):
                    QMessageBox.information(self, "Éxito", "Registro actualizado correctamente.")
                    TABLE_NAME = "LOGISTICA"
                    HEADERS = ["ID_Logistica", "Tipo", "Origen", "Destino", "Estado", "Fecha"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo actualizar el registro.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def eliminar_pedido(self):
        import db_manager
        
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un registro para eliminar.")
            return
        
        row = selected_rows[0].row()
        id_logistica = self.ui.tableWidget.item(row, 0).text()
        destino = self.ui.tableWidget.item(row, 3).text()
        
        reply = QMessageBox.question(
            self, 
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el registro logístico con destino {destino} (ID: {id_logistica})?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if db_manager.delete_record("LOGISTICA", "ID_Logistica", int(id_logistica)):
                QMessageBox.information(self, "Éxito", "Registro eliminado correctamente.")
                TABLE_NAME = "LOGISTICA"
                HEADERS = ["ID_Logistica", "Tipo", "Origen", "Destino", "Estado", "Fecha"]
                self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el registro.")
        
    @Slot()
    def ver_pedido(self):
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un registro para ver.")
            return
        
        row = selected_rows[0].row()
        detalles = []
        headers = ["ID_Logistica", "Tipo", "Origen", "Destino", "Estado", "Fecha"]
        for col in range(self.ui.tableWidget.columnCount()):
            valor = self.ui.tableWidget.item(row, col).text()
            detalles.append(f"{headers[col]}: {valor}")
        
        QMessageBox.information(self, "Detalles del Registro", "\n".join(detalles))
    
    @Slot()
    def buscar_pedido(self):
        from PySide6.QtWidgets import QInputDialog
        texto, ok = QInputDialog.getText(self, "Buscar", "Ingrese tipo, origen, destino o estado a buscar:")
        if ok and texto:
            for row in range(self.ui.tableWidget.rowCount()):
                match = False
                for col in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    if item and texto.lower() in item.text().lower():
                        match = True
                        break
                self.ui.tableWidget.setRowHidden(row, not match)
    
    @Slot()
    def ordenar_pedido(self):
        from PySide6.QtWidgets import QInputDialog
        columnas = ["ID_Logistica", "Tipo", "Origen", "Destino", "Estado", "Fecha"]
        columna, ok = QInputDialog.getItem(self, "Ordenar", "Seleccione columna:", columnas, 0, False)
        if ok:
            col_idx = columnas.index(columna)
            self.ui.tableWidget.sortItems(col_idx)
    
    @Slot()
    def admin_view(self):
        # Solo permitir acceder a la vista CEO si el usuario que pulsa es el CEO
        usuario = getattr(self, "current_user", None)
        if usuario == "CEO":
            # emitimos la señal con el nombre del usuario (AppManager lo recibirá)
            self.CEO.emit(usuario)
        else:
            QMessageBox.warning(self, "Acceso denegado", "Solo el CEO puede usar este botón.")
    
    def Logout_requested(self):
        self.logout_requested.emit()