import sys
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_e_movilidad import Ui_Widget 

# La clase MyWidget es tu vista de RRHH
class E_MovilidadWidget(QWidget):
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
            icon_edit = load_pixmap("edit.png")
            self.ui.botonEditar1.setIcon(icon_edit)
            icon_close = load_pixmap("close.png")
            self.ui.botonSacar1.setIcon(icon_close)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
            self.ui.botonAgregar.clicked.connect(self.agregar_equipo)
            self.ui.botonEditar1.clicked.connect(self.editar_equipo)
            self.ui.botonSacar1.clicked.connect(self.eliminar_equipo)
            self.ui.botonBuscar.clicked.connect(self.buscar_equipo)
            self.ui.lineEdit.textChanged.connect(self.buscar_equipo)
            self.ui.botonBorrar.clicked.connect(self.borrar_busqueda)
            self.ui.botonOrdenar1.clicked.connect(self.ordenar_equipo)
            self.ui.botonAdmin.clicked.connect(self.admin_view)
            self.ui.botonLogOut.clicked.connect(self.Logout_requested)

    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        self.current_user = username
        print(f"Usuario {username} ha ingresado a E-Movilidad.") # Impresión de prueba

            

    @Slot()
    def agregar_equipo(self):
        QMessageBox.information(self, "E-Movilidad", "Función: Agregar equipo.")

    @Slot()
    def editar_equipo(self):
        QMessageBox.information(self, "E-Movilidad", "Función: Editar equipo"
        ".")

    @Slot()
    def eliminar_equipo(self):
        QMessageBox.information(self, "E-Movilidad", "Función: Eliminar equipo.")

    @Slot()
    def buscar_equipo(self):
        texto = self.ui.lineEdit.text().strip()
        
        if not texto:
            # Si el campo está vacío, mostrar todas las filas
            if hasattr(self.ui, 'tableWidget'):
                for row in range(self.ui.tableWidget.rowCount()):
                    self.ui.tableWidget.setRowHidden(row, False)
            return
        
        if hasattr(self.ui, 'tableWidget'):
            for row in range(self.ui.tableWidget.rowCount()):
                match = False
                for col in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    if item and texto.lower() in item.text().lower():
                        match = True
                        break
                self.ui.tableWidget.setRowHidden(row, not match)

    @Slot()
    def temperatura_equipo(self):
        QMessageBox.information(self, "E-Movilidad", "Función: Chequear temperatura del equipo.")

    @Slot()
    def progreso_equipo(self):
        QMessageBox.information(self, "E-Movilidad", "Función: Chequear progreso del equipo.")

    @Slot()
    def ordenar_equipo(self):
        QMessageBox.information(self, "E-Movilidad", "Función: Ordenar equipo.")

    @Slot()
    def borrar_busqueda(self):
        self.ui.lineEdit.clear()
        if hasattr(self.ui, 'tableWidget'):
            for row in range(self.ui.tableWidget.rowCount()):
                self.ui.tableWidget.setRowHidden(row, False)

    @Slot()
    def ver_equipo(self):
        QMessageBox.information(self, "RRHH", "Función: Ver empleado.")
    
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