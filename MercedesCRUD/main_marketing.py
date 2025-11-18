import sys
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_marketing import Ui_Widget 
import db_manager

# La clase MyWidget es tu vista de RRHH
class MarketingWidget(QWidget):
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
            icon_edit = QIcon(load_pixmap("edit.png"))
            self.ui.botonEditar1.setIcon(icon_edit)
            icon_close = QIcon(load_pixmap("close.png"))
            self.ui.botonSacar1.setIcon(icon_close)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
            self.ui.botonAgregar.clicked.connect(self.agregar_campana)
            self.ui.botonEditar1.clicked.connect(self.editar_campana)
            self.ui.botonSacar1.clicked.connect(self.eliminar_campana)
            self.ui.botonBuscar.clicked.connect(self.buscar_campana)
            self.ui.botonBorrar.clicked.connect(self.borrar_busqueda)
            self.ui.botonOrdenar1.clicked.connect(self.ordenar_campana)
            self.ui.botonVer1.clicked.connect(self.ver_campana)
            self.ui.botonAdmin.clicked.connect(self.admin_view)
            self.ui.botonLogOut.clicked.connect(self.Logout_requested)

            # Comentado temporalmente hasta que se agreguen datos a CAMPANAS_MARKETING
            # TABLE_NAME = "CAMPANAS_MARKETING"
            # HEADERS = ["ID_Campana", "Tipo", "Estado", "Fecha_Inicio", "Fecha_Fin"]
            # UI_TABLE = self.ui.tableWidget
            # self.load_sector_data(TABLE_NAME, HEADERS, UI_TABLE)

        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        # self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        self.current_user = username
        print(f"Usuario {username} ha ingresado a Marketing.") # Impresión de prueba

        

    @Slot()
    def agregar_campana(self):
        QMessageBox.information(self, "Marketing", "Función: Agregar campaña.")

    @Slot()
    def editar_campana(self):
        QMessageBox.information(self, "Marketing", "Función: Editar campaña"
        ".")

    @Slot()
    def eliminar_campana(self):
        QMessageBox.information(self, "Marketing", "Función: Eliminar campaña.")

    @Slot()
    def buscar_campana(self):
        QMessageBox.information(self, "Marketing", "Función: Buscar campaña.")

    @Slot()
    def borrar_busqueda(self):
        QMessageBox.information(self, "Marketing", "Función: Borrar búsqueda.")
    
    @Slot()
    def ver_campana(self):
        QMessageBox.information(self, "Marketing", "Función: Ver campaña.")

    @Slot()
    def ordenar_campana(self):
        QMessageBox.information(self, "Marketing", "Función: Ordenar campaña.")
    
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
                from PySide6.QtWidgets import QTableWidgetItem
                cell_item = QTableWidgetItem(str(item))
                table_widget.setItem(row_idx, col_idx, cell_item)