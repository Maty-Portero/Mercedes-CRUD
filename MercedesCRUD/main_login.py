import sys
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from ui_login import Ui_Widget 

# La clase MyWidget es tu vista de Login
class LoginWidget(QWidget):
    # Define la señal que se emitirá cuando el login sea exitoso. 
    # Le pasamos el nombre de usuario (str) como argumento.
    login_successful = Signal(str) 

    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # AQUI AGREGAMOS EL ESTILO HOVER PARA EL BOTON 'Registrar' (pushButton)
        self.ui.pushButton.setStyleSheet("""
            QPushButton#pushButton {
                border: 2px solid #000000;
                border-radius: 15px;
                padding: 5px;
                color: black;
                background-color: #ebebeb;
            }
            QPushButton#pushButton:hover {
                border: 3px solid #000000;
                background-color: #d1d1d1;
            }
        """)
        
        # AQUI AGREGAMOS EL ESTILO HOVER PARA EL BOTON 'Iniciar sesion' (pushButton_2)
        self.ui.pushButton_2.setStyleSheet("""
            QPushButton#pushButton_2 {
                background-color: rgb(0, 45, 107);
                color: white;
                border: 2px solid #002d6b;
                border-radius: 15px;
                padding: 5px;
            }
            QPushButton#pushButton_2:hover {
                background-color: rgb(0, 30, 80);
                border: 2px solid #001f52;
            }
        """)

        # Conecta el botón 'Registrar' a una función
        self.ui.pushButton.clicked.connect(self.registrarme)
        
        # Conecta el botón 'Iniciar sesión' a la función
        self.ui.pushButton_2.clicked.connect(self.iniciar_sesion)

    @Slot()
    def iniciar_sesion(self):
        usuario = self.ui.lineEdit.text().strip()
        contrasena = self.ui.lineEdit_2.text().strip()
        
        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        # >>> LÓGICA DE VALIDACIÓN DE CREDENCIALES <<<
        # Aquí se conectaría a la base de datos o API. Usamos una simple validación de ejemplo:
        if usuario == "admin" and contrasena == "123":
            # Si el login es exitoso:
            self.login_successful.emit(usuario) # EMITIMOS la señal con el nombre de usuario
        else:
            # Si falla:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos.")
            
    @Slot()
    def registrarme(self):
        # Aquí puedes agregar la lógica para cambiar a la vista de registro si existiera,
        # o simplemente el proceso de registro.
        QMessageBox.information(self, "Registro", "Iniciando proceso de registro...")
        # Por ahora, solo imprime.
        print(f"Intento de registro de usuario - Usuario: {self.ui.lineEdit.text()}")