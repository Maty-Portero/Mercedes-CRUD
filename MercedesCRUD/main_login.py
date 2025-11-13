import sys
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPixmap 
from ui_login import Ui_Widget 
from db_manager import execute_query

# La clase MyWidget es tu vista de Login
class LoginWidget(QWidget):
    # Define la señal que se emitirá cuando el login sea exitoso. 
    # Le pasamos el nombre de usuario (str) como argumento.
    CEO = Signal(str)
    RRHH = Signal(str)
    Compras = Signal(str)
    Ventas = Signal(str)
    Produccion = Signal(str)
    Mantenimiento = Signal(str)
    Marketing = Signal(str)
    E_movilidad = Signal(str)
    Logistica = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # AQUI AGREGAMOS EL ESTILO HOVER PARA EL BOTON 'Iniciar sesion' (pushButton_2)
        self.ui.botonIniciar.setStyleSheet("""
            QPushButton#botonIniciar {
                background-color: rgb(0, 45, 107);
                color: white;
                border: 2px solid #002d6b;
                border-radius: 15px;
                padding: 5px;
            }
            QPushButton#botonIniciar:hover {
                background-color: rgb(0, 30, 80);
                border: 2px solid #001f52;
            }
        """)

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
        
        # Conecta el botón 'Iniciar sesión' a la función
        self.ui.botonIniciar.clicked.connect(self.iniciar_sesion)

    @Slot()
    def iniciar_sesion(self):
        usuario = self.ui.lineEdit.text().strip()
        contrasena = self.ui.lineEdit_2.text().strip()
        
        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        if usuario == "CEO" and contrasena == "prueba":
            self.CEO.emit(usuario)

        # >>> CONSULTA A LA BASE DE DATOS PARA VALIDAR CREDENCIALES Y OBTENER SECTOR <<<
        sql_query = f"SELECT sector FROM usuarios WHERE usuario = '{usuario}' AND contrasena = '{contrasena}'"
        query = execute_query(sql_query)
        
        if query and query.next():
            # Si el usuario existe y la contraseña es correcta
            sector = query.value(0)  # Obtiene el sector del usuario
            
            # Mapeo de sectores a sus respectivas señales
            sector_signal_map = {
                "RRHH": self.RRHH,
                "Compras": self.Compras,
                "Ventas": self.Ventas,
                "Produccion": self.Produccion,
                "Mantenimiento": self.Mantenimiento,
                "Marketing": self.Marketing,
                "E_movilidad": self.E_movilidad,
                "Logistica": self.Logistica
            }
            
            # Obtiene la señal correspondiente al sector y la emite
            if sector in sector_signal_map:
                sector_signal_map[sector].emit(usuario)
            else:
                QMessageBox.critical(self, "Error", f"Sector desconocido: {sector}")
        else:
            # Si falla:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos.") 