import sys
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_produccion import Ui_Widget 

# La clase MyWidget es tu vista de RRHH
class ProduccionTareasWidget(QWidget):
    # Señal para notificar al manager que el usuario quiere cerrar sesión
    logout_requested = Signal()
    CEO=Signal(str)
    produccion_almacen=Signal(str)
    # Asumo que tienes un QLabel para mostrar el saludo de bienvenida en tu UI
    # Si no lo tienes, puedes agregarlo en el diseñador de Qt.
    def __init__(self):
            super().__init__()
            self.ui = Ui_Widget()
            self.ui.setupUi(self)

            # Carga de imágenes optimizada
            self.ui.label_5.setPixmap(load_pixmap("logo.png"))
            self.ui.label_5.setScaledContents(True)
            self.ui.label_7.setPixmap(load_pixmap("perfil-de-usuario.png"))
            self.ui.label_7.setScaledContents(True)
            from PySide6.QtGui import QIcon
            icon_edit = QIcon(load_pixmap("edit.png"))
            self.ui.botonEditar1.setIcon(icon_edit)
            icon_close = QIcon(load_pixmap("close.png"))
            self.ui.botonSacar1.setIcon(icon_close)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
            self.ui.botonAgregar.clicked.connect(self.agregar_equipo)
            self.ui.botonEditar1.clicked.connect(self.editar_equipo)
            self.ui.botonSacar1.clicked.connect(self.eliminar_equipo)
            self.ui.botonBuscar.clicked.connect(self.buscar_equipo)
            self.ui.botonOrdenar1.clicked.connect(self.ordenar_equipo)
            self.ui.botonBorrar.clicked.connect(self.borrar_busqueda)
            self.ui.botonAdmin.clicked.connect(self.admin_view)
            self.ui.botonLogOut.clicked.connect(self.Logout_requested)
            self.ui.botonAlmacen.clicked.connect(self.IrAlmacen)

            import db_manager
            TABLE_NAME = "PRODUCCION_TAREAS"
            HEADERS = ["ID_Tarea", "Descripcion", "Responsable", "Estado", "Fecha_Inicio", "Fecha_Fin"]
            UI_TABLE = self.ui.tableWidget
            self.load_sector_data(TABLE_NAME, HEADERS, UI_TABLE)
            
        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        # self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        self.current_user = username
        print(f"Usuario {username} ha ingresado a Produccion.") # Impresión de prueba

        

    @Slot()
    def agregar_equipo(self):
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        import db_manager
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Tarea de Producción")
        layout = QFormLayout()
        
        descripcion_input = QLineEdit()
        responsable_input = QLineEdit()
        estado_input = QLineEdit()
        fecha_inicio_input = QLineEdit()
        fecha_fin_input = QLineEdit()
        
        layout.addRow("Descripción:", descripcion_input)
        layout.addRow("Responsable:", responsable_input)
        layout.addRow("Estado:", estado_input)
        layout.addRow("Fecha Inicio (YYYY-MM-DD):", fecha_inicio_input)
        layout.addRow("Fecha Fin (YYYY-MM-DD):", fecha_fin_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["Descripcion", "Responsable", "Estado", "Fecha_Inicio", "Fecha_Fin"]
                values = [
                    descripcion_input.text(),
                    responsable_input.text(),
                    estado_input.text(),
                    fecha_inicio_input.text() if fecha_inicio_input.text() else None,
                    fecha_fin_input.text() if fecha_fin_input.text() else None
                ]
                
                if db_manager.insert_record("PRODUCCION_TAREAS", columns, values):
                    QMessageBox.information(self, "Éxito", "Tarea agregada correctamente.")
                    TABLE_NAME = "PRODUCCION_TAREAS"
                    HEADERS = ["ID_Tarea", "Descripcion", "Responsable", "Estado", "Fecha_Inicio", "Fecha_Fin"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo agregar la tarea.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def editar_equipo(self):
        import db_manager
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione una tarea para editar.")
            return
        
        row = selected_rows[0].row()
        id_tarea = self.ui.tableWidget.item(row, 0).text()
        descripcion_actual = self.ui.tableWidget.item(row, 1).text()
        responsable_actual = self.ui.tableWidget.item(row, 2).text()
        estado_actual = self.ui.tableWidget.item(row, 3).text()
        fecha_inicio_actual = self.ui.tableWidget.item(row, 4).text()
        fecha_fin_actual = self.ui.tableWidget.item(row, 5).text()
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Editar Tarea de Producción")
        layout = QFormLayout()
        
        descripcion_input = QLineEdit(descripcion_actual)
        responsable_input = QLineEdit(responsable_actual)
        estado_input = QLineEdit(estado_actual)
        fecha_inicio_input = QLineEdit(fecha_inicio_actual)
        fecha_fin_input = QLineEdit(fecha_fin_actual)
        
        layout.addRow("Descripción:", descripcion_input)
        layout.addRow("Responsable:", responsable_input)
        layout.addRow("Estado:", estado_input)
        layout.addRow("Fecha Inicio (YYYY-MM-DD):", fecha_inicio_input)
        layout.addRow("Fecha Fin (YYYY-MM-DD):", fecha_fin_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["Descripcion", "Responsable", "Estado", "Fecha_Inicio", "Fecha_Fin"]
                values = [
                    descripcion_input.text(),
                    responsable_input.text(),
                    estado_input.text(),
                    fecha_inicio_input.text() if fecha_inicio_input.text() else None,
                    fecha_fin_input.text() if fecha_fin_input.text() else None
                ]
                
                if db_manager.update_record("PRODUCCION_TAREAS", columns, values, "ID_Tarea", int(id_tarea)):
                    QMessageBox.information(self, "Éxito", "Tarea actualizada correctamente.")
                    TABLE_NAME = "PRODUCCION_TAREAS"
                    HEADERS = ["ID_Tarea", "Descripcion", "Responsable", "Estado", "Fecha_Inicio", "Fecha_Fin"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo actualizar la tarea.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def eliminar_equipo(self):
        import db_manager
        
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione una tarea para eliminar.")
            return
        
        row = selected_rows[0].row()
        id_tarea = self.ui.tableWidget.item(row, 0).text()
        descripcion = self.ui.tableWidget.item(row, 1).text()
        
        reply = QMessageBox.question(
            self, 
            "Confirmar eliminación",
            f"¿Está seguro de eliminar la tarea '{descripcion}' (ID: {id_tarea})?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if db_manager.delete_record("PRODUCCION_TAREAS", "ID_Tarea", int(id_tarea)):
                QMessageBox.information(self, "Éxito", "Tarea eliminada correctamente.")
                TABLE_NAME = "PRODUCCION_TAREAS"
                HEADERS = ["ID_Tarea", "Descripcion", "Responsable", "Estado", "Fecha_Inicio", "Fecha_Fin"]
                self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar la tarea.")

    @Slot()
    def buscar_equipo(self):
        from PySide6.QtWidgets import QInputDialog
        texto, ok = QInputDialog.getText(self, "Buscar Tarea", "Ingrese descripción, responsable o estado a buscar:")
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
    def progreso_equipo(self):
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione una tarea para ver el progreso.")
            return
        
        row = selected_rows[0].row()
        detalles = []
        headers = ["ID_Tarea", "Descripción", "Responsable", "Estado", "Fecha Inicio", "Fecha Fin"]
        for col in range(self.ui.tableWidget.columnCount()):
            valor = self.ui.tableWidget.item(row, col).text()
            detalles.append(f"{headers[col]}: {valor}")
        
        QMessageBox.information(self, "Progreso de Tarea", "\n".join(detalles))

    @Slot()
    def borrar_busqueda(self):
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.setRowHidden(row, False)

    @Slot()
    def abrir_alerta(self):
        QMessageBox.information(self, "Produccion", "Función: Abrir Alerta.")

    @Slot()
    def ordenar_equipo(self):
        from PySide6.QtWidgets import QInputDialog
        columnas = ["ID_Tarea", "Descripcion", "Responsable", "Estado", "Fecha_Inicio", "Fecha_Fin"]
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
    
    def IrAlmacen(self):
        usuario = getattr(self, "current_user", None)
        self.produccion_almacen.emit(usuario)
        
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
            self.ui.label_14.setText(f"Órdenes: {len(data)}")
    
