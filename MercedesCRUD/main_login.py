import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_login import Ui_Widget # Asegúrate de que este sea el nombre correcto del archivo generado.

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Crea una instancia de la clase de interfaz de usuario generada
        self.ui = Ui_Widget()
        # Configura la interfaz en tu widget principal
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
        
        # Conecta el botón 'Iniciar sesión' a una función
        self.ui.pushButton_2.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        # Esta es la función que se ejecutará cuando el botón sea clickeado
        usuario = self.ui.lineEdit.text()
        contrasena = self.ui.lineEdit_2.text()
        print(f"Intento de inicio de sesión - Usuario: {usuario}, Contraseña: {contrasena}")
        # Aquí puedes agregar la lógica de validación o conexión a base de datos.
        
    def registrarme(self):
        # Esta es la función que se ejecutará cuando el botón sea clickeado
        usuario = self.ui.lineEdit.text()
        contrasena = self.ui.lineEdit_2.text()
        print(f"Intento de registro de usuario - Usuario: {usuario}, Contraseña: {contrasena}")
        # Aquí puedes agregar la lógica de validación o conexión a base de datos.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())