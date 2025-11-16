from PySide6.QtGui import QPixmap
import os

# Simple in-memory cache for loaded QPixmaps to avoid re-reading disk repeatedly.
_IMAGE_CACHE = {}


def load_pixmap(image_name, base_dir=None, use_cache=True):
    """Load a QPixmap by name with optional in-memory caching.

    Args:
        image_name (str): Filename of the image (e.g. "logo.png").
        base_dir (str|None): Directory to resolve the image from. If None uses this module's dir.
        use_cache (bool): If True, return a cached QPixmap when available.

    Returns:
        QPixmap: The loaded pixmap (may be null if loading failed).
    """
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    key = (image_name, base_dir)
    if use_cache and key in _IMAGE_CACHE:
        return _IMAGE_CACHE[key]

    image_path = os.path.join(base_dir, image_name)
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        print(f"[ERROR DE IMAGEN] No se pudo cargar '{image_name}' en '{image_path}'")

    if use_cache:
        _IMAGE_CACHE[key] = pixmap

    return pixmap


def preload_images(image_names, base_dir=None):
    """Pre-load a list of image names into the cache.

    Args:
        image_names (Iterable[str]): list of filenames to preload.
        base_dir (str|None): directory to resolve files from.
    """
    for name in image_names:
        load_pixmap(name, base_dir=base_dir, use_cache=True)


def clear_cache():
    """Clear the in-memory image cache."""
    _IMAGE_CACHE.clear()
