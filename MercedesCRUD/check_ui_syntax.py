import os
import sys
import glob
import importlib.util

UI_DIR = os.path.dirname(__file__)
PATTERN = os.path.join(UI_DIR, 'ui_*.py')

errors = []

for ui_file in glob.glob(PATTERN):
    try:
        spec = importlib.util.spec_from_file_location("ui_module", ui_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        errors.append((ui_file, str(e)))

if errors:
    print("Errores de sintaxis/indentación en archivos UI:")
    for fname, err in errors:
        print(f"{fname}: {err}")
    sys.exit(1)
else:
    print("Todos los archivos ui_*.py se importaron correctamente.")
    sys.exit(0)
