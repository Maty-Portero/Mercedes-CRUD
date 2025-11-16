import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_e_movilidad_ceo import Ui_Widget

# La clase MyWidget es tu vista de RRHH
class E_MovilidadCEOWidget(QWidget):
    # Señal para notificar al manager que el usuario quiere cerrar sesión
    # Asumo que tienes un QLabel para mostrar el saludo de bienvenida en tu UI
    # Si no lo tienes, puedes agregarlo en el diseñador de Qt.
    CEO=Signal(str)
    e_movilidad_ceo_registro=Signal(str)
    e_movilidad_ceo_usuarios_autorizados=Signal(str)
    logout_requested = Signal()
    E_movilidad = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Carga de imágenes optimizada
        self.ui.label_5.setPixmap(load_pixmap("logo.png"))
        self.ui.label_5.setScaledContents(True)
        self.ui.label_8.setPixmap(load_pixmap("perfil-de-usuario.png"))
        self.ui.label_8.setScaledContents(True)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        #self.ui.botonCompras.clicked.connect(self.ir_db)
        #self.ui.botonLogistica.clicked.connect(self.ir_registro)
        #self.ui.botonE_movilidad.clicked.connect(self.ir_usuarios_autorizados)
        
        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        # self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
        self.ui.botonAdmin.clicked.connect(self.admin_view)
        self.ui.botonAdmin.clicked.connect(self.admin_view)
        self.ui.botonLogOut.clicked.connect(self.Logout_requested)
        self.ui.botonRegistro.clicked.connect(self.ir_registro)
        self.ui.botonUsuarioAutorizados.clicked.connect(self.ir_usuarios_autorizados)
        self.ui.botonDB.clicked.connect(self.ir_db)
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        self.current_user = username
        print(f"Usuario {username} ha ingresado a CEO.") # Impresión de prueba
    
    def Logout_requested(self):
        self.logout_requested.emit()

    @Slot()
    def admin_view(self):
        # Solo permitir acceder a la vista CEO si el usuario que pulsa es el CEO
        usuario = getattr(self, "current_user", None)
        if usuario == "CEO":
            # emitimos la señal con el nombre del usuario (AppManager lo recibirá)
            self.CEO.emit(usuario)
        else:
            QMessageBox.warning(self, "Acceso denegado", "Solo el CEO puede usar este botón.")
    
    @Slot()
    def ir_registro(self):
        usuario = getattr(self, "current_user", None)
        self.e_movilidad_ceo_registro.emit(usuario)
    
    @Slot()
    def ir_usuarios_autorizados(self):
        usuario = getattr(self, "current_user", None)
        self.e_movilidad_ceo_usuarios_autorizados.emit(usuario)
    
    @Slot()
    def ir_db(self):
        usuario = getattr(self, "current_user", None)
        self.E_movilidad.emit(usuario)
    
    def Logout_requested(self):
        self.logout_requested.emit()