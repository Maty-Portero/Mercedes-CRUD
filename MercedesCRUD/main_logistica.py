import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPixmap 
from ui_logistica import Ui_Widget

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
        image_path = os.path.join(script_dir, "edit.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'edit.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.botonEditar1.setIcon(pixmap)
        self.ui.botonEditar2.setIcon(pixmap)
        self.ui.botonEditar3.setIcon(pixmap)

        # 1. Obtiene la ruta del directorio donde se encuentra este archivo de código (LoginWidget)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construye la ruta completa al archivo (Ej: C:/MiProyecto/mercedes.png)
        image_path = os.path.join(script_dir, "close.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'close.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.botonSacar1.setIcon(pixmap)
        self.ui.botonSacar2.setIcon(pixmap)
        self.ui.botonSacar3.setIcon(pixmap)

        # 1. Obtiene la ruta del directorio donde se encuentra este archivo de código (LoginWidget)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construye la ruta completa al archivo (Ej: C:/MiProyecto/mercedes.png)
        image_path = os.path.join(script_dir, "eye.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'eye.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.botonVer1.setIcon(pixmap)
        self.ui.botonVer2.setIcon(pixmap)
        self.ui.botonVer3.setIcon(pixmap)


        # 1. Obtiene la ruta del directorio donde se encuentra este archivo de código (LoginWidget)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construye la ruta completa al archivo (Ej: C:/MiProyecto/mercedes.png)
        image_path = os.path.join(script_dir, "c.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'c.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.botonAgregar.setIcon(pixmap)

        # 1. Obtiene la ruta del directorio donde se encuentra este archivo de código (LoginWidget)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construye la ruta completa al archivo (Ej: C:/MiProyecto/mercedes.png)
        image_path = os.path.join(script_dir, "down_arrow.png") 
        
        # 3. Crea el QPixmap
        pixmap = QPixmap(image_path)

        # 4. COMPRUEBA si la carga fue exitosa
        if pixmap.isNull():
            print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
            print(f"Ruta COMPLETA intentada: {image_path}")
            print(f"Asegúrate de que el nombre de archivo sea exactamente 'down_arrow.png' y que el archivo exista en esa ubicación.")
        else:
            print(f"Imagen cargada OK desde: {image_path}")
        # ----------------------------------------------------

        # 5. Asigna el pixmap al QLabel 'label'
        self.ui.botonOrdenar1.setIcon(pixmap)

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