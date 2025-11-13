import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from PySide6.QtCore import Slot
from PySide6.QtSql import QSqlDatabase

# IMPORTANTE: Importamos las clases renombradas de los archivos
# Asegúrate de que los archivos main_login.py y main_rrhh.py estén en la misma carpeta.
from main_login import LoginWidget 
from main_rrhh import RRHHWidget
from main_ceo import CEOWidget
from main_e_movilidad import E_MovilidadWidget
from main_e_movilidad_ceo_db import E_MovilidadCEOdbWidget
from main_e_movilidad_ceo_registro import E_MovilidadCEOregistroWidget
from main_e_movilidad_ceo import E_MovilidadCEOWidget
from main_compras import ComprasWidget
from main_marketing import MarketingWidget
from main_produccion_tareas import ProduccionTareasWidget
from main_produccion_almacen import ProduccionAlmacenWidget
from main_ventas import VentasWidget
from main_logistica import LogisticaWidget
from main_mantenimiento import MantenimientoWidget

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
        self.ceo_view = CEOWidget()
        self.e_movilidad_view = E_MovilidadWidget()
        self.e_movilidad_ceo_db_view = E_MovilidadCEOdbWidget()
        self.e_movilidad_ceo_registro_view = E_MovilidadCEOregistroWidget()
        self.e_movilidad_ceo_view = E_MovilidadCEOWidget()
        self.compras_view = ComprasWidget()
        self.marketing_view = MarketingWidget()
        self.produccion_tareas_view = ProduccionTareasWidget()
        self.produccion_almacen_view = ProduccionAlmacenWidget()
        self.ventas_view = VentasWidget()
        self.logistica_view = LogisticaWidget()
        self.mantenimiento_view = MantenimientoWidget()
        
        # Añadir las vistas y guardar sus índices
        self.LOGIN_INDEX = self.stack.addWidget(self.login_view)
        self.RRHH_INDEX = self.stack.addWidget(self.rrhh_view)
        self.CEO_INDEX = self.stack.addWidget(self.ceo_view)
        self.E_MOVILIDAD_INDEX = self.stack.addWidget(self.e_movilidad_view)
        self.E_MOVILIDAD_CEO_DB_INDEX = self.stack.addWidget(self.e_movilidad_ceo_db_view)
        self.E_MOVILIDAD_CEO_REG_INDEX = self.stack.addWidget(self.e_movilidad_ceo_registro_view)
        self.E_MOVILIDAD_CEO_INDEX = self.stack.addWidget(self.e_movilidad_ceo_view)
        self.COMPRAS_INDEX = self.stack.addWidget(self.compras_view)
        self.MARKETING_INDEX = self.stack.addWidget(self.marketing_view)
        self.PRODUCCION_TAREAS_INDEX = self.stack.addWidget(self.produccion_tareas_view)
        self.PRODUCCION_ALMACEN_INDEX = self.stack.addWidget(self.produccion_almacen_view)
        self.VENTAS_INDEX = self.stack.addWidget(self.ventas_view)
        self.LOGISTICA_INDEX = self.stack.addWidget(self.logistica_view)
        self.MANTENIMIENTO_INDEX = self.stack.addWidget(self.mantenimiento_view)

        # 3. Conectar la lógica de navegación
        self.mantenimiento_view.logout_requested.connect(self.show_login_view)
        self.rrhh_view.logout_requested.connect(self.show_login_view)
        self.ceo_view.logout_requested.connect(self.show_login_view)
        self.e_movilidad_view.logout_requested.connect(self.show_login_view)
        self.e_movilidad_ceo_db_view.logout_requested.connect(self.show_login_view)
        self.e_movilidad_ceo_registro_view.logout_requested.connect(self.show_login_view)
        self.e_movilidad_ceo_view.logout_requested.connect(self.show_login_view)
        self.compras_view.logout_requested.connect(self.show_login_view)
        self.marketing_view.logout_requested.connect(self.show_login_view)
        self.produccion_tareas_view.logout_requested.connect(self.show_login_view)
        self.produccion_almacen_view.logout_requested.connect(self.show_login_view)
        self.ventas_view.logout_requested.connect(self.show_login_view)
        self.logistica_view.logout_requested.connect(self.show_login_view)

        
        self.login_view.RRHH.connect(self.show_rrhh_view)

        self.login_view.Mantenimiento.connect(self.show_mantenimiento_view)

        self.login_view.Ventas.connect(self.show_ventas_view)

        self.login_view.Compras.connect(self.show_compras_view)

        self.login_view.Produccion.connect(self.show_produccion_view)

        self.login_view.E_movilidad.connect(self.show_e_movilidad_view)

        self.login_view.Marketing.connect(self.show_marketing_view)

        self.login_view.Logistica.connect(self.show_logistica_view)

        self.login_view.CEO.connect(self.show_ceo_view)
        
        self.ceo_view.Mantenimiento.connect(self.show_mantenimiento_view)

        self.ceo_view.RRHH.connect(self.show_rrhh_view)

        self.ceo_view.Logistica.connect(self.show_logistica_view)
        
        self.ceo_view.Compras.connect(self.show_compras_view)
        
        self.ceo_view.Ventas.connect(self.show_ventas_view)
        
        self.ceo_view.Produccion.connect(self.show_produccion_view)
        
        self.ceo_view.Marketing.connect(self.show_marketing_view)
        
        self.ceo_view.E_movilidad.connect(self.show_e_movilidad_view)
        
        self.rrhh_view.CEO.connect(self.show_ceo_view)

        self.mantenimiento_view.CEO.connect(self.show_ceo_view)

        self.marketing_view.CEO.connect(self.show_ceo_view)

        self.logistica_view.CEO.connect(self.show_ceo_view)

        self.compras_view.CEO.connect(self.show_ceo_view)

        self.ventas_view.CEO.connect(self.show_ceo_view)

        self.e_movilidad_view.CEO.connect(self.show_ceo_view)

        self.produccion_tareas_view.CEO.connect(self.show_ceo_view)

        # 4. Iniciar la aplicación en la vista de Login
        self.show_login_view() 

    @Slot()
    def show_login_view(self):
        """Cambia el QStackedWidget a la vista de Login."""
        self.stack.setCurrentIndex(self.LOGIN_INDEX)
        self.setWindowTitle("Sistema de Gestión - Inicio de Sesión")
    
    # ...existing code...
    @Slot(str)
    def show_mantenimiento_view(self, username):
        self.mantenimiento_view.set_welcome_message(username)
        self.stack.setCurrentIndex(self.MANTENIMIENTO_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - Mantenimiento ({username})")

    @Slot(str)
    def show_logistica_view(self, username):
        self.logistica_view.set_welcome_message(username)
        self.stack.setCurrentIndex(self.LOGISTICA_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - Logística ({username})")

    @Slot(str)
    def show_marketing_view(self, username):
        self.marketing_view.set_welcome_message(username)
        self.stack.setCurrentIndex(self.MARKETING_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - Marketing ({username})")

    @Slot(str)
    def show_ventas_view(self, username):
        self.ventas_view.set_welcome_message(username)
        self.stack.setCurrentIndex(self.VENTAS_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - Ventas ({username})")

    @Slot(str)
    def show_compras_view(self, username):
        self.compras_view.set_welcome_message(username)
        self.stack.setCurrentIndex(self.COMPRAS_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - Compras ({username})")

    @Slot(str)
    def show_e_movilidad_view(self, username):
        self.e_movilidad_view.set_welcome_message(username)
        self.stack.setCurrentIndex(self.E_MOVILIDAD_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - E-Movilidad ({username})")

    @Slot(str)
    def show_produccion_view(self, username):
        # Si tienes dos vistas de producción (tareas/almacén) ajusta según necesites
        self.produccion_tareas_view.set_welcome_message(username)
        self.stack.setCurrentIndex(self.PRODUCCION_TAREAS_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - Producción ({username})")

    @Slot(str) 
    def show_rrhh_view(self, username):
        """Muestra el widget Principal de RRHH y le envía el nombre del usuario."""
        
        # Llama a un método en la vista de RRHH para actualizar su contenido
        self.rrhh_view.set_welcome_message(username)
        
        self.stack.setCurrentIndex(self.RRHH_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - RRHH de {username}")

    @Slot(str) 
    def show_ceo_view(self, username):
        """Muestra el widget Principal de CEO y le envía el nombre del usuario."""
        
        # Llama a un método en la vista de RRHH para actualizar su contenido
        self.ceo_view.set_welcome_message(username)
        
        self.stack.setCurrentIndex(self.CEO_INDEX)
        self.setWindowTitle(f"Sistema de Gestión - CEO de {username}")


if __name__ == "__main__":
    # La inicialización de la aplicación y el loop principal (exec())
    app = QApplication(sys.argv)
    manager = AppManager()
    manager.show()
    sys.exit(app.exec())
