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

        # Conecta el botón 'Iniciar sesión' a una función (ejemplo)
        # Observa que el nombre del botón en tu UI es 'pushButton_2'
        self.ui.pushButton.clicked.connect(self.registrarme)
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