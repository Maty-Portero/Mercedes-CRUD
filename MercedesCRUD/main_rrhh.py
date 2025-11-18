import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_rrhh import Ui_Widget

# La clase MyWidget es tu vista de RRHH
class RRHHWidget(QWidget):

    # Señal para notificar al manager que el usuario quiere cerrar sesión
    logout_requested = Signal()
    CEO = Signal(str)
    # Asumo que tienes un QLabel para mostrar el saludo de bienvenida en tu UI
    # Si no lo tienes, puedes agregarlo en el diseñador de Qt.

    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        # Carga de imágenes optimizada
        self.ui.label_5.setPixmap(load_pixmap("logo.png"))
        self.ui.label_5.setScaledContents(True)
        self.ui.label_8.setPixmap(load_pixmap("perfil-de-usuario.png"))
        self.ui.label_8.setScaledContents(True)
        from PySide6.QtGui import QIcon
        icon_edit = QIcon(load_pixmap("edit.png"))
        self.ui.botonEditar1.setIcon(icon_edit)
        icon_close = QIcon(load_pixmap("close.png"))
        self.ui.botonSacar1.setIcon(icon_close)
        self.ui.botonAgregar.setIcon(QIcon(load_pixmap("c.png")))
        self.ui.botonOrdenar1.setIcon(QIcon(load_pixmap("down_arrow.png")))

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        self.ui.botonAgregar.clicked.connect(self.agregar_empleado)
        self.ui.botonEditar1.clicked.connect(self.editar_empleado)
        self.ui.botonSacar1.clicked.connect(self.eliminar_empleado)
        self.ui.botonBuscar.clicked.connect(self.buscar_empleado)
        self.ui.lineEdit.textChanged.connect(self.buscar_empleado)
        self.ui.botonOrdenar1.clicked.connect(self.ordenar_empleado)
        self.ui.botonAdmin.clicked.connect(self.admin_view)
        self.ui.botonLogOut.clicked.connect(self.Logout_requested)

        import db_manager
        TABLE_NAME = "RRHH"
        HEADERS = ["ID_RRHH", "ID_Empleado", "Tipo_Evento", "Fecha", "Descripcion"]
        UI_TABLE = self.ui.tableWidget
        self.load_sector_data(TABLE_NAME, HEADERS, UI_TABLE)
        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        #self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)
        y guarda el usuario actual para validaciones posteriores."""
        self.current_user = username  # guardamos el usuario que está usando la vista
        # Si tienes un QLabel con objectName 'label_welcome', usarlo:
        print(f"Usuario {username} ha ingresado a RRHH.") # Impresión de prueba


        

    @Slot()
    def agregar_empleado(self):
        from PySide6.QtWidgets import QInputDialog, QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        import db_manager
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Evento RRHH")
        layout = QFormLayout()
        
        # Crear campos de entrada para la nueva estructura
        id_empleado_input = QLineEdit()
        tipo_evento_input = QLineEdit()
        fecha_input = QLineEdit()
        descripcion_input = QLineEdit()
        
        layout.addRow("ID Empleado:", id_empleado_input)
        layout.addRow("Tipo Evento:", tipo_evento_input)
        layout.addRow("Fecha (YYYY-MM-DD):", fecha_input)
        layout.addRow("Descripción:", descripcion_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["ID_Empleado", "Tipo_Evento", "Fecha", "Descripcion"]
                values = [
                    int(id_empleado_input.text()),
                    tipo_evento_input.text(),
                    fecha_input.text(),
                    descripcion_input.text()
                ]
                
                if db_manager.insert_record("RRHH", columns, values):
                    QMessageBox.information(self, "Éxito", "Evento agregado correctamente.")
                    # Recargar tabla
                    TABLE_NAME = "RRHH"
                    HEADERS = ["ID_RRHH", "ID_Empleado", "Tipo_Evento", "Fecha", "Descripcion"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo agregar el evento.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def editar_empleado(self):
        import db_manager
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        
        # Obtener fila seleccionada
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un evento para editar.")
            return
        
        row = selected_rows[0].row()
        
        # Obtener datos actuales (5 columnas: ID_RRHH, ID_Empleado, Tipo_Evento, Fecha, Descripcion)
        id_rrhh = self.ui.tableWidget.item(row, 0).text()
        id_empleado_actual = self.ui.tableWidget.item(row, 1).text()
        tipo_evento_actual = self.ui.tableWidget.item(row, 2).text()
        fecha_actual = self.ui.tableWidget.item(row, 3).text()
        descripcion_actual = self.ui.tableWidget.item(row, 4).text()
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Editar Evento RRHH")
        layout = QFormLayout()
        
        id_empleado_input = QLineEdit(id_empleado_actual)
        tipo_evento_input = QLineEdit(tipo_evento_actual)
        fecha_input = QLineEdit(fecha_actual)
        descripcion_input = QLineEdit(descripcion_actual)
        
        layout.addRow("ID Empleado:", id_empleado_input)
        layout.addRow("Tipo Evento:", tipo_evento_input)
        layout.addRow("Fecha (YYYY-MM-DD):", fecha_input)
        layout.addRow("Descripción:", descripcion_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["ID_Empleado", "Tipo_Evento", "Fecha", "Descripcion"]
                values = [
                    int(id_empleado_input.text()),
                    tipo_evento_input.text(),
                    fecha_input.text(),
                    descripcion_input.text()
                ]
                
                if db_manager.update_record("RRHH", columns, values, "ID_RRHH", int(id_rrhh)):
                    QMessageBox.information(self, "Éxito", "Evento actualizado correctamente.")
                    # Recargar tabla
                    TABLE_NAME = "RRHH"
                    HEADERS = ["ID_RRHH", "ID_Empleado", "Tipo_Evento", "Fecha", "Descripcion"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo actualizar el evento.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def eliminar_empleado(self):
        import db_manager
        
        # Obtener fila seleccionada
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un empleado para eliminar.")
            return
        
        row = selected_rows[0].row()
        id_rrhh = self.ui.tableWidget.item(row, 0).text()
        tipo_evento = self.ui.tableWidget.item(row, 2).text()
        
        # Confirmar eliminación
        reply = QMessageBox.question(
            self, 
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el evento {tipo_evento} (ID: {id_rrhh})?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if db_manager.delete_record("RRHH", "ID_RRHH", int(id_rrhh)):
                QMessageBox.information(self, "Éxito", "Evento eliminado correctamente.")
                # Recargar tabla
                TABLE_NAME = "RRHH"
                HEADERS = ["ID_RRHH", "ID_Empleado", "Tipo_Evento", "Fecha", "Descripcion"]
                self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el evento.")
        
    @Slot()
    def ver_empleado(self):
        # Obtener fila seleccionada
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un empleado para ver.")
            return
        
        row = selected_rows[0].row()
        
        # Obtener todos los datos de la fila
        detalles = []
        headers = ["ID_RRHH", "ID_Empleado", "Tipo_Evento", "Fecha", "Descripción"]
        for col in range(self.ui.tableWidget.columnCount()):
            valor = self.ui.tableWidget.item(row, col).text()
            detalles.append(f"{headers[col]}: {valor}")
        
        QMessageBox.information(self, "Detalles del Evento", "\n".join(detalles))

    @Slot()
    def buscar_empleado(self):
        texto = self.ui.lineEdit.text().strip()
        
        if not texto:
            # Si el campo está vacío, mostrar todas las filas
            for row in range(self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.setRowHidden(row, False)
            return
        
        # Buscar en todas las columnas
        for row in range(self.ui.tableWidget.rowCount()):
            match = False
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item and texto.lower() in item.text().lower():
                    match = True
                    break
            
            # Ocultar/mostrar filas según el criterio
            self.ui.tableWidget.setRowHidden(row, not match)
    
    @Slot()
    def ordenar_empleado(self):
        from PySide6.QtWidgets import QInputDialog
        
        columnas = ["ID_RRHH", "ID_Empleado", "Tipo_Evento", "Fecha", "Descripción"]
        columna, ok = QInputDialog.getItem(self, "Ordenar", "Seleccione columna para ordenar:", columnas, 0, False)
        
        if ok:
            col_index = columnas.index(columna)
            self.ui.tableWidget.sortItems(col_index)
    
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

    def load_sector_data(self, table_name, headers, table_widget):
        """
        Carga datos en el QTableWidget del sector usando db_manager.
        """
        import db_manager
        from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
        from PySide6.QtCore import Qt
        try:
            data = db_manager.get_data_for_sector(table_name, headers)
            if data is None:
                QMessageBox.critical(self, "Error de BD", f"La consulta a la tabla '{table_name}' falló o no devolvió datos.")
                return
        except Exception as e:
            QMessageBox.critical(self, "Error de BD", f"Error al cargar datos de {table_name}: {e}")
            return
        if not hasattr(table_widget, 'setColumnCount'):
            print(f"[WARN] El widget proporcionado para mostrar la tabla ('{table_name}') no es una QTableWidget. Saltando carga.")
            return
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        table_widget.setRowCount(0)
        table_widget.setRowCount(len(data))

        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                cell_item = QTableWidgetItem(str(item))
                cell_item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, cell_item)
        
        # Estilo y configuración de tamaños
        header = table_widget.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table_widget.verticalHeader().setDefaultSectionSize(40)
        table_widget.horizontalHeader().setMinimumHeight(40)
        table_widget.setStyleSheet("""
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
            self.ui.label_14.setText(f"Empleados: {len(data)}")