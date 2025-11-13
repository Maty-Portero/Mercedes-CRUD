import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPixmap 
from ui_ceo_home import Ui_Widget

# La clase MyWidget es tu vista de RRHH
class CEOWidget(QWidget):
    # Señal para notificar al manager que el usuario quiere cerrar sesión
    # Asumo que tienes un QLabel para mostrar el saludo de bienvenida en tu UI
    # Si no lo tienes, puedes agregarlo en el diseñador de Qt.
    RRHH = Signal(str)
    Compras = Signal(str)
    Ventas = Signal(str)
    Produccion = Signal(str)
    Mantenimiento = Signal(str)
    Marketing = Signal(str)
    E_movilidad = Signal(str)
    Logistica = Signal(str)
    logout_requested = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # 1. Obtiene la ruta del directorio donde se encuentra este archivo de código (LoginWidget)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construye la ruta completa al archivo (Ej: C:/MiProyecto/mercedes.png)
        image_path = os.path.join(script_dir, "logo.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'logo.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.label_5.setPixmap(pixmap)
        self.ui.label_5.setScaledContents(True) # Aseguramos que escale

        # 1. Obtiene la ruta del directorio donde se encuentra este archivo de código (LoginWidget)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construye la ruta completa al archivo (Ej: C:/MiProyecto/mercedes.png)
        image_path = os.path.join(script_dir, "perfil-de-usuario.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'perfil-de-usuario.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.label_7.setPixmap(pixmap)
        self.ui.label_7.setScaledContents(True) # Aseguramos que escale

        # 1. Obtiene la ruta del directorio donde se encuentra este archivo de código (LoginWidget)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construye la ruta completa al archivo (Ej: C:/MiProyecto/mercedes.png)
        image_path = os.path.join(script_dir, "mercedes.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'mercedes.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setScaledContents(True) # Aseguramos que escale

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
        self.ui.botonCompras.clicked.connect(self.IrCompras)
        self.ui.botonLogistica.clicked.connect(self.IrLogistica)
        self.ui.botonE_movilidad.clicked.connect(self.IrE_movilidad)
        self.ui.botonMantenimiento.clicked.connect(self.IrMantenimiento)
        self.ui.botonMarketing.clicked.connect(self.IrMarketing)
        self.ui.botonProduccion.clicked.connect(self.IrProduccion)
        self.ui.botonVentas.clicked.connect(self.IrVentas)
        self.ui.botonRRHH.clicked.connect(self.IrRRHH)
        self.ui.botonLogOut.clicked.connect(self.Logout_requested)

        # Conexión CLAVE: El botón que hace de "Cerrar Sesión"
        # Asumo que el botón 7 es el de Cerrar Sesión
        # self.ui.pushButton_7.clicked.connect(self.logout_requested.emit)
    
    def IrCompras(self):
        self.Compras.emit("CEO")
    def IrLogistica(self):
        self.Logistica.emit("CEO")
    def IrProduccion(self):
        self.Produccion.emit("CEO")
    def IrE_movilidad(self):
        self.E_movilidad.emit("CEO")
    def IrMantenimiento(self):
        self.Mantenimiento.emit("CEO")
    def IrMarketing(self):
        self.Marketing.emit("CEO")
    def IrVentas(self):
        self.Ventas.emit("CEO")
    def IrRRHH(self):
        self.RRHH.emit("CEO")
    def Logout_requested(self):
        self.logout_requested.emit()
        
    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        print(f"Usuario {username} ha ingresado a CEO.") # Impresión de prueba
    