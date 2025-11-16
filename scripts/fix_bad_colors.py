import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'MercedesCRUD'
if not root.exists():
    print('ERROR: folder MercedesCRUD not found at', root)
    sys.exit(1)

pattern = re.compile(r'#00000(?![0-9A-Fa-f])')
replacements = 0
for path in root.rglob('*'):
    if path.is_file() and path.suffix.lower() in ('.py', '.ui'):
        text = path.read_text(encoding='utf-8', errors='ignore')
        new_text, count = pattern.subn('#000000', text)
        if count:
            path.write_text(new_text, encoding='utf-8')
            print(f'Patched {count} occurrences in {path.relative_to(root.parent)}')
            replacements += count

print(f'Done. Total replacements: {replacements}')
