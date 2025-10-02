import sys
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from ui_rrhh import Ui_Widget

# La clase MyWidget es tu vista de RRHH
class RRHHWidget(QWidget):
    # Señal para notificar al manager que el usuario quiere cerrar sesión
    logout_requested = Signal()
    # Asumo que tienes un QLabel para mostrar el saludo de bienvenida en tu UI
    # Si no lo tienes, puedes agregarlo en el diseñador de Qt.

    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        self.ui.botonAgregar.clicked.connect(self.agregar_empleado)
        self.ui.botonEditar1.clicked.connect(self.editar_empleado)
        self.ui.botonEditar2.clicked.connect(self.editar_empleado)
        self.ui.botonEditar3.clicked.connect(self.editar_empleado)
        self.ui.botonSacar1.clicked.connect(self.eliminar_empleado)
        self.ui.botonSacar2.clicked.connect(self.eliminar_empleado)
        self.ui.botonSacar3.clicked.connect(self.eliminar_empleado)
        
        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        # self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        print(f"Usuario {username} ha ingresado a RRHH.") # Impresión de prueba

    @Slot()
    def agregar_empleado(self):
        QMessageBox.information(self, "RRHH", "Función: Agregar empleado.")

    @Slot()
    def editar_empleado(self):
        QMessageBox.information(self, "RRHH", "Función: Editar empleado.")

    @Slot()
    def eliminar_empleado(self):
        QMessageBox.information(self, "RRHH", "Función: Eliminar empleado.")