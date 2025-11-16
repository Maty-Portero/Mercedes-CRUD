import sys, os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtGui import QPixmap 
from ui_logistica import Ui_Widget
from image_loader import load_pixmap
import db_manager

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

        self.ui.label_5.setPixmap(load_pixmap("logo.png"))
        self.ui.label_5.setScaledContents(True)
        self.ui.label_7.setPixmap(load_pixmap("perfil-de-usuario.png"))
        self.ui.label_7.setScaledContents(True)
        icon_edit = load_pixmap("edit.png")
        self.ui.botonEditar1.setIcon(icon_edit)
        icon_close = load_pixmap("close.png")
        self.ui.botonSacar1.setIcon(icon_close)
        icon_eye = load_pixmap("eye.png")
        self.ui.botonVer1.setIcon(icon_eye)
        self.ui.botonAgregar.setIcon(load_pixmap("c.png"))
        self.ui.botonOrdenar1.setIcon(load_pixmap("down_arrow.png"))
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

        TABLE_NAME = "SEGUIMIENTO_LOGISTICO"
        HEADERS = ["ID_Seguimiento", "Tipo_Logistica", "Origen", "Destino", "Estado_Actual", "ID_Pedido_OC"]
        UI_TABLE = self.ui.tableWidget # Asegúrate de que este sea el objectName correcto
        
        # Llamada para cargar los datos
        self.load_sector_data(TABLE_NAME, HEADERS, UI_TABLE)
    
    def load_sector_data(self, table_name, headers, table_widget):
        """
        Función reutilizable para cargar datos en la QTableWidget del sector.
        Utiliza el módulo db_manager para obtener los datos.
        """
        
        # 1. Obtener los datos usando la función del manager
        try:
            # Llamamos a la función generalizada en el módulo db_manager
            data = db_manager.get_data_for_sector(table_name, headers)
            
            if data is None:
                 QMessageBox.critical(self, "Error de BD", f"La consulta a la tabla '{table_name}' falló o no devolvió datos.")
                 return
                 
        except Exception as e:
            QMessageBox.critical(self, "Error de BD", f"Error al cargar datos de {table_name}: {e}")
            return

        # 2. Configurar la QTableWidget
        table_widget.setColumnCount(len(headers))
        # Mostrar los nombres de las columnas en la cabecera de la tabla
        table_widget.setHorizontalHeaderLabels(headers) 
        
        table_widget.setRowCount(0) 
        table_widget.setRowCount(len(data)) 

        # 3. Poblar la tabla
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                cell_item = QTableWidgetItem(str(item))
                cell_item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row_idx, col_idx, cell_item)
                
        # Estilo final
        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.resizeColumnsToContents()
        print(f"Sector {table_name}: {len(data)} registros cargados.")

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
        self.ui.botonSacar1.clicked.connect(self.eliminar_pedido)
        self.ui.botonVer1.clicked.connect(self.ver_pedido)
        self.ui.botonBuscar.clicked.connect(self.buscar_pedido)
        self.ui.botonOrdenar1.clicked.connect(self.ordenar_pedido)
        self.ui.botonAdmin.clicked.connect(self.admin_view)
        self.ui.botonLogOut.clicked.connect(self.Logout_requested)

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
    
    def Logout_requested(self):
        self.logout_requested.emit()