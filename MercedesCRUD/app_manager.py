import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import Slot

# IMPORTANTE: Importamos las clases renombradas de los archivos
# Asegúrate de que los archivos main_login.py y main_rrhh.py estén en la misma carpeta.
from main_login import LoginWidget 
from main_rrhh import RRHHWidget

class AppManager(QMainWindow):
    """
    Ventana principal que utiliza QStackedWidget para gestionar todas las vistas 
    de la aplicación en un solo proceso.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión Centralizada")
        self.setGeometry(100, 100, 800, 600) 
        self.showFullScreen()

        # 1. Crear el contenedor de vistas (QStackedWidget)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # 2. Instanciar y añadir las vistas
        # Cada vista ahora es un objeto Widget que se gestiona aquí
        self.login_view = LoginWidget()
        self.rrhh_view = RRHHWidget()
        
        # Añadir las vistas y guardar sus índices
        self.LOGIN_INDEX = self.stack.addWidget(self.login_view) # Índice 0
        self.RRHH_INDEX = self.stack.addWidget(self.rrhh_view)   # Índice 1

        # 3. Conectar la lógica de navegación
        
        # Si la vista de Login EMITE la señal 'login_successful', llamamos a show_rrhh_view
        self.login_view.login_successful.connect(self.show_rrhh_view)
        
        # Si la vista de RRHH EMITE la señal 'logout_requested', volvemos al login
        self.rrhh_view.logout_requested.connect(self.show_login_view)

        # 4. Iniciar la aplicación en la vista de Login
        self.show_login_view() 

    @Slot()
    def show_login_view(self):
        """Cambia el QStackedWidget a la vista de Login."""
        self.stack.setCurrentIndex(self.LOGIN_INDEX)
        self.setWindowTitle("Sistema de Gestión - Inicio de Sesión")

    @Slot(str) 
    def show_rrhh_view(self, username):
        """Muestra el widget Principal de RRHH y le envía el nombre del usuario."""
        
        # Llama a un método en la vista de RRHH para actualizar su contenido
        self.rrhh_view.set_welcome_message(username)
        
        self.stack.setCurrentIndex(self.RRHH_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - RRHH de {username}")


if __name__ == "__main__":
    # La inicialización de la aplicación y el loop principal (exec())
    app = QApplication(sys.argv)
    manager = AppManager()
    manager.show()
    sys.exit(app.exec())
