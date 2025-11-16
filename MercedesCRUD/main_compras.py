import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_compras import Ui_Widget

# La clase MyWidget es tu vista de RRHH
class ComprasWidget(QWidget):
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
        icon_eye = load_pixmap("eye.png")
        self.ui.botonVer1.setIcon(icon_eye)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        self.ui.botonAgregar.clicked.connect(self.agregar_orden)
        self.ui.botonEditar1.clicked.connect(self.editar_orden)
        self.ui.botonSacar1.clicked.connect(self.eliminar_orden)
        self.ui.botonVer1.clicked.connect(self.ver_orden)
        self.ui.botonBuscar.clicked.connect(self.buscar_orden)
        self.ui.botonOrdenar1.clicked.connect(self.ordenar_orden)
        self.ui.botonAdmin.clicked.connect(self.admin_view)
        self.ui.botonLogOut.clicked.connect(self.Logout_requested)

        
        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        #self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        self.current_user = username
        print(f"Usuario {username} ha ingresado a Compras.") # Impresión de prueba

        

    @Slot()
    def agregar_orden(self):
        QMessageBox.information(self, "Compras", "Función: Agregar orden.")

    @Slot()
    def editar_orden(self):
        QMessageBox.information(self, "Compras", "Función: Editar orden.")

    @Slot()
    def eliminar_orden(self):
        QMessageBox.information(self, "Compras", "Función: Eliminar orden.")

    @Slot()
    def ver_orden(self):
        QMessageBox.information(self, "Compras", "Función: Ver orden.")

    @Slot()
    def buscar_orden(self):
        QMessageBox.information(self, "Compras", "Función: Buscar orden.")
    
    @Slot()
    def ordenar_orden(self):
        QMessageBox.information(self, "Compras", "Función: Ordenar orden.")
    
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