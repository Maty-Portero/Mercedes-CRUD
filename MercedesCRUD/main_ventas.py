import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_ventas import Ui_Widget

# La clase MyWidget es tu vista de RRHH
class VentasWidget(QWidget):
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
        self.ui.botonEditar2.setIcon(icon_edit)
        self.ui.botonEditar3.setIcon(icon_edit)
        icon_close = load_pixmap("close.png")
        self.ui.botonSacar1.setIcon(icon_close)
        self.ui.botonSacar2.setIcon(icon_close)
        self.ui.botonSacar3.setIcon(icon_close)
        icon_eye = load_pixmap("eye.png")
        self.ui.botonVer1.setIcon(icon_eye)
        self.ui.botonVer2.setIcon(icon_eye)
        self.ui.botonVer3.setIcon(icon_eye)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        self.ui.botonAgregar.clicked.connect(self.agregar_venta)
        self.ui.botonEditar1.clicked.connect(self.editar_venta)
        self.ui.botonEditar2.clicked.connect(self.editar_venta)
        self.ui.botonEditar3.clicked.connect(self.editar_venta)
        self.ui.botonEditar4.clicked.connect(self.editar_venta)
        self.ui.botonEditar5.clicked.connect(self.editar_venta)
        self.ui.botonEditar6.clicked.connect(self.editar_venta)
        self.ui.botonSacar1.clicked.connect(self.eliminar_venta)
        self.ui.botonSacar2.clicked.connect(self.eliminar_venta)
        self.ui.botonSacar3.clicked.connect(self.eliminar_venta)
        self.ui.botonSacar4.clicked.connect(self.eliminar_venta)
        self.ui.botonSacar5.clicked.connect(self.eliminar_venta)
        self.ui.botonSacar6.clicked.connect(self.eliminar_venta)
        self.ui.botonVer1.clicked.connect(self.ver_venta)
        self.ui.botonVer2.clicked.connect(self.ver_venta)
        self.ui.botonVer3.clicked.connect(self.ver_venta)
        self.ui.botonVer4.clicked.connect(self.ver_venta)
        self.ui.botonVer5.clicked.connect(self.ver_venta)
        self.ui.botonVer6.clicked.connect(self.ver_venta)
        self.ui.botonBuscar.clicked.connect(self.buscar_venta)
        self.ui.botonOrdenar1.clicked.connect(self.ordenar_venta)
        self.ui.botonAdmin.clicked.connect(self.admin_view)
        self.ui.botonLogOut.clicked.connect(self.Logout_requested)
        
        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        #self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        self.current_user = username
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        print(f"Usuario {username} ha ingresado a Ventas.") # Impresión de prueba

        

    @Slot()
    def agregar_venta(self):
        QMessageBox.information(self, "Ventas", "Función: Agregar venta.")

    @Slot()
    def editar_venta(self):
        QMessageBox.information(self, "Ventas", "Función: Editar venta.")

    @Slot()
    def eliminar_venta(self):
        QMessageBox.information(self, "Ventas", "Función: Eliminar venta.")

    @Slot()
    def ver_venta(self):
        QMessageBox.information(self, "Ventas", "Función: Ver venta.")

    @Slot()
    def buscar_venta(self):
        QMessageBox.information(self, "Compras", "Función: Buscar venta.")
    
    @Slot()
    def ordenar_venta(self):
        QMessageBox.information(self, "Compras", "Función: Ordenar venta.")

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