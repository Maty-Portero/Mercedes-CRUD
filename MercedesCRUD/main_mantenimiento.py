import sys
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_mantenimiento import Ui_Widget 
import db_manager

# La clase MyWidget es tu vista de RRHH
class MantenimientoWidget(QWidget):
    # Señal para notificar al manager que el usuario quiere cerrar sesión
    logout_requested = Signal()
    CEO=Signal(str)
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
            self.ui.botonEditar1.setIcon(QIcon(load_pixmap("edit.png")))
            self.ui.botonSacar1.setIcon(QIcon(load_pixmap("close.png")))
            self.ui.botonAgregar.setIcon(QIcon(load_pixmap("c.png")))
            self.ui.botonOrdenar1.setIcon(QIcon(load_pixmap("down_arrow.png")))
            self.ui.botonBuscar.setIcon(QIcon(load_pixmap("search.png")))
            self.ui.botonBorrar.setIcon(QIcon(load_pixmap("delete.png")))

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
            self.ui.botonAgregar.clicked.connect(self.agregar_equipo)
            self.ui.botonEditar1.clicked.connect(self.editar_equipo)
            self.ui.botonSacar1.clicked.connect(self.eliminar_equipo)
            self.ui.botonBuscar.clicked.connect(self.buscar_equipo)
            self.ui.lineEdit.textChanged.connect(self.buscar_equipo)
            self.ui.botonOrdenar1.clicked.connect(self.ordenar_equipo)
            self.ui.botonBorrar.clicked.connect(self.borrar_busqueda)
            self.ui.botonAdmin.clicked.connect(self.admin_view)
            self.ui.botonLogOut.clicked.connect(self.Logout_requested)

            TABLE_NAME = "MANTENIMIENTO_EQUIPOS"
            HEADERS = ["ID_Equipo", "Nombre", "Tipo", "Estado", "Ultima_Revision"]
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
        print(f"Usuario {username} ha ingresado a Mantenimiento.") # Impresión de prueba

        

    @Slot()
    def agregar_equipo(self):
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        import db_manager
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Equipo de Mantenimiento")
        layout = QFormLayout()
        
        nombre_input = QLineEdit()
        tipo_input = QLineEdit()
        estado_input = QLineEdit()
        ultima_revision_input = QLineEdit()
        
        layout.addRow("Nombre:", nombre_input)
        layout.addRow("Tipo:", tipo_input)
        layout.addRow("Estado:", estado_input)
        layout.addRow("Última Revisión (YYYY-MM-DD):", ultima_revision_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["Nombre", "Tipo", "Estado", "Ultima_Revision"]
                values = [
                    nombre_input.text(),
                    tipo_input.text(),
                    estado_input.text(),
                    ultima_revision_input.text()
                ]
                
                if db_manager.insert_record("MANTENIMIENTO_EQUIPOS", columns, values):
                    QMessageBox.information(self, "Éxito", "Equipo agregado correctamente.")
                    TABLE_NAME = "MANTENIMIENTO_EQUIPOS"
                    HEADERS = ["ID_Equipo", "Nombre", "Tipo", "Estado", "Ultima_Revision"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo agregar el equipo.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def editar_equipo(self):
        import db_manager
        from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
        
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un equipo para editar.")
            return
        
        row = selected_rows[0].row()
        id_equipo = self.ui.tableWidget.item(row, 0).text()
        nombre_actual = self.ui.tableWidget.item(row, 1).text()
        tipo_actual = self.ui.tableWidget.item(row, 2).text()
        estado_actual = self.ui.tableWidget.item(row, 3).text()
        revision_actual = self.ui.tableWidget.item(row, 4).text()
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Editar Equipo de Mantenimiento")
        layout = QFormLayout()
        
        nombre_input = QLineEdit(nombre_actual)
        tipo_input = QLineEdit(tipo_actual)
        estado_input = QLineEdit(estado_actual)
        revision_input = QLineEdit(revision_actual)
        
        layout.addRow("Nombre:", nombre_input)
        layout.addRow("Tipo:", tipo_input)
        layout.addRow("Estado:", estado_input)
        layout.addRow("Última Revisión (YYYY-MM-DD):", revision_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        
        dialog.setLayout(layout)
        
        if dialog.exec() == QDialog.Accepted:
            try:
                columns = ["Nombre", "Tipo", "Estado", "Ultima_Revision"]
                values = [
                    nombre_input.text(),
                    tipo_input.text(),
                    estado_input.text(),
                    revision_input.text()
                ]
                
                if db_manager.update_record("MANTENIMIENTO_EQUIPOS", columns, values, "ID_Equipo", int(id_equipo)):
                    QMessageBox.information(self, "Éxito", "Equipo actualizado correctamente.")
                    TABLE_NAME = "MANTENIMIENTO_EQUIPOS"
                    HEADERS = ["ID_Equipo", "Nombre", "Tipo", "Estado", "Ultima_Revision"]
                    self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
                else:
                    QMessageBox.critical(self, "Error", "No se pudo actualizar el equipo.")
            except ValueError as e:
                QMessageBox.warning(self, "Error de validación", f"Por favor ingrese valores válidos: {e}")

    @Slot()
    def eliminar_equipo(self):
        import db_manager
        
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un equipo para eliminar.")
            return
        
        row = selected_rows[0].row()
        id_equipo = self.ui.tableWidget.item(row, 0).text()
        nombre = self.ui.tableWidget.item(row, 1).text()
        
        reply = QMessageBox.question(
            self, 
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el equipo '{nombre}' (ID: {id_equipo})?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if db_manager.delete_record("MANTENIMIENTO_EQUIPOS", "ID_Equipo", int(id_equipo)):
                QMessageBox.information(self, "Éxito", "Equipo eliminado correctamente.")
                TABLE_NAME = "MANTENIMIENTO_EQUIPOS"
                HEADERS = ["ID_Equipo", "Nombre", "Tipo", "Estado", "Ultima_Revision"]
                self.load_sector_data(TABLE_NAME, HEADERS, self.ui.tableWidget)
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el equipo.")

    @Slot()
    def buscar_equipo(self):
        texto = self.ui.lineEdit.text().strip()
        
        if not texto:
            # Si el campo está vacío, mostrar todas las filas
            for row in range(self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.setRowHidden(row, False)
            return
        
        for row in range(self.ui.tableWidget.rowCount()):
            match = False
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item and texto.lower() in item.text().lower():
                    match = True
                    break
            self.ui.tableWidget.setRowHidden(row, not match)

    @Slot()
    def estado_equipo(self):
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione un equipo para ver el estado.")
            return
        
        row = selected_rows[0].row()
        detalles = []
        headers = ["ID_Equipo", "Nombre", "Tipo", "Estado", "Última Revisión"]
        for col in range(self.ui.tableWidget.columnCount()):
            valor = self.ui.tableWidget.item(row, col).text()
            detalles.append(f"{headers[col]}: {valor}")
        
        QMessageBox.information(self, "Estado del Equipo", "\n".join(detalles))

    @Slot()
    def borrar_busqueda(self):
        self.ui.lineEdit.clear()
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.setRowHidden(row, False)

    @Slot()
    def ordenar_equipo(self):
        from PySide6.QtWidgets import QInputDialog
        columnas = ["ID_Equipo", "Nombre", "Tipo", "Estado", "Ultima_Revision"]
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

    def load_sector_data(self, table_name, headers, table_widget):
        """
        Carga datos en el QTableWidget del sector usando db_manager.
        """
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
        
        # Configurar tabla como solo lectura y selección por fila completa
        table_widget.setEditTriggers(table_widget.EditTrigger.NoEditTriggers)
        table_widget.setSelectionBehavior(table_widget.SelectionBehavior.SelectRows)
        table_widget.setSelectionMode(table_widget.SelectionMode.SingleSelection)
        
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
            self.ui.label_14.setText(f"Equipos: {len(data)}")

    def some_method(self):
        TABLE_NAME = "MANTENIMIENTO_EQUIPOS"
        HEADERS = ["ID_Equipo", "Nombre", "Tipo", "Estado", "Ultima_Revision"]
        UI_TABLE = self.ui.tableWidget
        self.load_sector_data(TABLE_NAME, HEADERS, UI_TABLE)