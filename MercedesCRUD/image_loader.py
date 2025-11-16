from PySide6.QtGui import QPixmap
import os

def load_pixmap(image_name, base_dir=None):
    """
    Carga una imagen y devuelve un QPixmap. Si falla, devuelve un QPixmap vacío y muestra un error.
    Args:
        image_name (str): Nombre del archivo de imagen.
        base_dir (str): Directorio base. Si es None, usa el directorio actual.
    Returns:
        QPixmap
    """
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, image_name)
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        print(f"[ERROR DE IMAGEN] No se pudo cargar '{image_name}' en '{image_path}'")
    return pixmap
