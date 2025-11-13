import sys
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPixmap 
from ui_e_movilidad_ceo_db import Ui_Widget 

# La clase MyWidget es tu vista de RRHH
class E_MovilidadCEOdbWidget(QWidget):
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
            self.ui.label_17.setPixmap(pixmap)
            self.ui.label_17.setScaledContents(True) # Aseguramos que escale

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
            image_path = os.path.join(script_dir, "doc.svg") 
            
            # 3. Crea el QPixmap
            pixmap = QPixmap(image_path)

            # 4. COMPRUEBA si la carga fue exitosa
            if pixmap.isNull():
                print(f"\n[ERROR DE IMAGEN] NO SE PUDO CARGAR LA IMAGEN.")
                print(f"Ruta COMPLETA intentada: {image_path}")
                print(f"Asegúrate de que el nombre de archivo sea exactamente 'doc.svg' y que el archivo exista en esa ubicación.")
            else:
                print(f"Imagen cargada OK desde: {image_path}")
            # ----------------------------------------------------

            # 5. Asigna el pixmap al QLabel 'label'
            self.ui.botonDoc1.setIcon(pixmap)
            self.ui.botonDoc2.setIcon(pixmap)
            self.ui.botonDoc3.setIcon(pixmap)
            self.ui.botonDoc4.setIcon(pixmap)
            self.ui.botonDoc5.setIcon(pixmap)

        # >>> LÓGICA DE CONEXIÓN DE BOTONES ORIGINALES <<<
            self.ui.botonAgregar.clicked.connect(self.agregar_equipo)
            self.ui.botonEditar1.clicked.connect(self.editar_equipo)
            self.ui.botonEditar2.clicked.connect(self.editar_equipo)
            self.ui.botonEditar3.clicked.connect(self.editar_equipo)
            self.ui.botonEditar4.clicked.connect(self.editar_equipo)
            self.ui.botonEditar5.clicked.connect(self.editar_equipo)
            self.ui.botonSacar1.clicked.connect(self.eliminar_equipo)
            self.ui.botonSacar2.clicked.connect(self.eliminar_equipo)
            self.ui.botonSacar3.clicked.connect(self.eliminar_equipo)
            self.ui.botonSacar4.clicked.connect(self.eliminar_equipo)
            self.ui.botonSacar5.clicked.connect(self.eliminar_equipo)
            self.ui.botonBuscar.clicked.connect(self.buscar_equipo)
            self.ui.botonBorrar.clicked.connect(self.borrar_busqueda)
            self.ui.botonOrdenar1.clicked.connect(self.ordenar_equipo)
            self.ui.botonProgreso1.clicked.connect(self.progreso_equipo)
            self.ui.botonProgreso2.clicked.connect(self.progreso_equipo)
            self.ui.botonProgreso3.clicked.connect(self.progreso_equipo)
            self.ui.botonProgreso4.clicked.connect(self.progreso_equipo)
            self.ui.botonProgreso5.clicked.connect(self.progreso_equipo)
            self.ui.botonTemp1.clicked.connect(self.temperatura_equipo)
            self.ui.botonTemp2.clicked.connect(self.temperatura_equipo)
            self.ui.botonTemp3.clicked.connect(self.temperatura_equipo)
            self.ui.botonTemp4.clicked.connect(self.temperatura_equipo)
            self.ui.botonTemp5.clicked.connect(self.temperatura_equipo)
            self.ui.botonVer1.clicked.connect(self.ver_equipo)
            self.ui.botonVer2.clicked.connect(self.ver_equipo)
            self.ui.botonVer3.clicked.connect(self.ver_equipo)
            self.ui.botonDoc1.clicked.connect(self.abrir_registro)
            self.ui.botonDoc2.clicked.connect(self.abrir_registro)
            self.ui.botonDoc3.clicked.connect(self.abrir_registro)
            self.ui.botonDoc4.clicked.connect(self.abrir_registro)
            self.ui.botonDoc5.clicked.connect(self.abrir_registro)
            self.ui.botonAdmin.clicked.connect(self.admin_view)

    # Método para recibir y establecer el nombre de usuario (Llamado desde AppManager)
    def set_welcome_message(self, username):
        """Muestra el mensaje de bienvenida en un QLabel (asumiendo que tienes uno)."""
        # Si tienes un QLabel con objectName 'label_welcome', lo usarías así:
        # self.ui.label_welcome.setText(f"Bienvenido, {username}")
        self.current_user = username
        print(f"Usuario {username} ha ingresado a E-Movilidad CEO.") # Impresión de prueba

            

    @Slot()
    def agregar_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Agregar equipo.")

    @Slot()
    def editar_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Editar equipo"
        ".")

    @Slot()
    def eliminar_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Eliminar equipo.")

    @Slot()
    def buscar_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Buscar equipo.")

    @Slot()
    def temperatura_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Chequear temperatura del equipo.")

    @Slot()
    def progreso_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Chequear progreso del equipo.")

    @Slot()
    def ordenar_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Ordenar equipo.")

    @Slot()
    def borrar_busqueda(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Borrar búsqueda.")

    @Slot()
    def ver_equipo(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Ver empleado.")

    @Slot()
    def abrir_registro(self):
        QMessageBox.information(self, "E-Movilidad CEO", "Función: Abrir Registro.")
    
    @Slot()
    def admin_view(self):
        # Solo permitir acceder a la vista CEO si el usuario que pulsa es el CEO
        usuario = getattr(self, "current_user", None)
        if usuario == "CEO":
            # emitimos la señal con el nombre del usuario (AppManager lo recibirá)
            self.CEO.emit(usuario)
        else:
            QMessageBox.warning(self, "Acceso denegado", "Solo el CEO puede usar este botón.")