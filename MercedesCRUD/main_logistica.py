import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from ui_logistica import Ui_Widget
from image_loader import load_pixmap

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
        self.ui.botonAgregar.setIcon(load_pixmap("c.png"))
        self.ui.botonOrdenar1.setIcon(load_pixmap("down_arrow.png"))

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        self.ui.botonAgregar.clicked.connect(self.agregar_pedido)
        self.ui.botonEditar1.clicked.connect(self.editar_pedido)
        self.ui.botonEditar2.clicked.connect(self.editar_pedido)
        self.ui.botonEditar3.clicked.connect(self.editar_pedido)
        self.ui.botonSacar1.clicked.connect(self.eliminar_pedido)
        self.ui.botonSacar2.clicked.connect(self.eliminar_pedido)
        self.ui.botonSacar3.clicked.connect(self.eliminar_pedido)
        self.ui.botonVer1.clicked.connect(self.ver_pedido)
        self.ui.botonVer2.clicked.connect(self.ver_pedido)
        self.ui.botonVer3.clicked.connect(self.ver_pedido)
        self.ui.botonBuscar.clicked.connect(self.buscar_pedido)
        self.ui.botonOrdenar1.clicked.connect(self.ordenar_pedido)
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
        print(f"Usuario {username} ha ingresado a Logistica.") # Impresión de prueba

        

    @Slot()
    def agregar_pedido(self):
        QMessageBox.information(self, "Logistica", "Función: Agregar Pedido.")

    @Slot()
    def editar_pedido(self):
        QMessageBox.information(self, "Logistica", "Función: Editar Pedido.")

    @Slot()
    def eliminar_pedido(self):
        QMessageBox.information(self, "Logistica", "Función: Eliminar Pedido.")
        
    @Slot()
    def ver_pedido(self):
        QMessageBox.information(self, "Logistica", "Función: Ver Pedido.")
    
    @Slot()
    def buscar_pedido(self):
        QMessageBox.information(self, "Compras", "Función: Buscar Pedido.")
    
    @Slot()
    def ordenar_pedido(self):
        QMessageBox.information(self, "Compras", "Función: Ordenar Pedido.")
    
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