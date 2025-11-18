import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from ui_e_movilidad_ceo_registro import Ui_Widget

# La clase MyWidget es tu vista de RRHH
class E_MovilidadCEOregistroWidget(QWidget):
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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.ui.label_5.setPixmap(load_pixmap("logo.png"))
        self.ui.label_5.setScaledContents(True)
        self.ui.label_8.setPixmap(load_pixmap("perfil-de-usuario.png"))
        self.ui.label_8.setScaledContents(True)
        from PySide6.QtGui import QIcon
        icon_edit = QIcon(load_pixmap("edit.png"))
        self.ui.botonEditar1.setIcon(icon_edit)
        icon_close = QIcon(load_pixmap("close.png"))
        self.ui.botonSacar1.setIcon(icon_close)
        icon_c = QIcon(load_pixmap("c.png"))
        self.ui.botonAgregar.setIcon(icon_c)
        icon_down_arrow = QIcon(load_pixmap("down_arrow.png"))
        self.ui.botonOrdenar1.setIcon(icon_down_arrow)
        
        # 3. Crea el QPixmap

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        self.ui.botonAgregar.clicked.connect(self.agregar_empleado)
        self.ui.botonEditar1.clicked.connect(self.editar_empleado)
        self.ui.botonSacar1.clicked.connect(self.eliminar_empleado)
        self.ui.botonBuscar.clicked.connect(self.buscar_empleado)
        self.ui.lineEdit.textChanged.connect(self.buscar_empleado)
        self.ui.botonOrdenar1.clicked.connect(self.ordenar_empleado)
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
        
    @Slot()
    def ver_empleado(self):
        QMessageBox.information(self, "RRHH", "Función: Ver empleado.")

    @Slot()
    def buscar_empleado(self):
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
    def ordenar_empleado(self):
        QMessageBox.information(self, "Compras", "Función: Ordenar empleado.")
    
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