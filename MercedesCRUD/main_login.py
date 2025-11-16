import sys
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from image_loader import load_pixmap
from PySide6.QtCore import Qt
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

        # Carga de imágenes optimizada
        self.ui.label.setPixmap(load_pixmap("mercedes.png"))
        self.ui.label.setScaledContents(True)
        self.ui.label_5.setPixmap(load_pixmap("logo.png"))
        self.ui.label_5.setScaledContents(True)
        
        # Conecta el botón 'Iniciar sesión' a la función
        self.ui.botonIniciar.clicked.connect(self.iniciar_sesion)
        
        # Conectar eventos de tecla Enter en los campos de texto
        self.ui.lineEdit.returnPressed.connect(self.on_email_return_pressed)
        self.ui.lineEdit_2.returnPressed.connect(self.iniciar_sesion)

    @Slot()
    def on_email_return_pressed(self):
        """Al presionar Enter en el email, enfocarse en la contraseña"""
        self.ui.lineEdit_2.setFocus()

    @Slot()
    def iniciar_sesion(self):
        usuario = self.ui.lineEdit.text().strip()
        contrasena = self.ui.lineEdit_2.text().strip()
        
        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        if usuario == "CEO" and contrasena == "prueba":
            self.CEO.emit(usuario)
            return  
            
        # Consulta a la BD con parámetros (evita SQL injection)
        sql_query = """
            SELECT S.Nombre_Sector 
            FROM USUARIOS AS U 
            INNER JOIN SECTORES AS S ON U.ID_Sector = S.ID_Sector 
            WHERE U.Nombre_Usuario = ? AND U.Contrasena = ?
        """
        query = execute_query(sql_query, (usuario, contrasena))
        
        print(f"DEBUG: Usuario={usuario}, Contraseña={contrasena}")  # DEBUG
        print(f"DEBUG: Query result={query}")  # DEBUG
        
        if query and query.next():
            sector = query.value(0)
            print(f"DEBUG: Sector encontrado='{sector}'")  # DEBUG
            
            sector_signal_map = {
                "RRHH": self.RRHH,
                "Compras": self.Compras,
                "Ventas": self.Ventas,
                "Producción": self.Produccion,
                "Mantenimiento": self.Mantenimiento,
                "Marketing": self.Marketing,
                "E-Movilidad": self.E_movilidad,
                "Logística": self.Logistica,
            }
            
            print(f"DEBUG: Keys disponibles={list(sector_signal_map.keys())}")  # DEBUG
            
            if sector in sector_signal_map:
                sector_signal_map[sector].emit(usuario)
            else:
                QMessageBox.critical(self, "Error", f"Sector desconocido: '{sector}' (disponibles: {list(sector_signal_map.keys())})")
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos.")