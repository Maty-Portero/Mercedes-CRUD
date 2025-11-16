"""Scan all ui_*.py files under MercedesCRUD, try to compile them, and attempt a conservative
fix for IndentationError/unexpected indent by aligning the error line to the previous
non-empty line's indentation. Prints a report and writes fixed files in-place.

This script makes conservative changes; please review diffs/commits afterwards.
"""
import sys
from pathlib import Path
import traceback

root = Path(__file__).resolve().parents[1] / 'MercedesCRUD'
if not root.exists():
    print('ERROR: MercedesCRUD not found at', root)
    sys.exit(1)

ui_files = sorted(root.glob('ui_*.py'))
if not ui_files:
    print('No ui_*.py files found')
    sys.exit(0)

fixed_files = []
problems = []

for f in ui_files:
    text = f.read_text(encoding='utf-8')
    try:
        compile(text, str(f), 'exec')
        continue
    except IndentationError as ie:
        problems.append((f, ie))
    except SyntaxError as se:
        # if it's not indentation-related, record and skip
        problems.append((f, se))

for f, err in problems:
    print('Processing', f)
    lines = f.read_text(encoding='utf-8').splitlines()
    lineno = getattr(err, 'lineno', None)
    msg = getattr(err, 'msg', str(err))
    print('  Error:', type(err).__name__, 'line', lineno, msg)
    if lineno is None:
        continue
    idx = lineno - 1
    if idx < 0 or idx >= len(lines):
        continue

    # Conservative fix heuristic for 'unexpected indent': dedent the error line to match previous
    # non-empty line indentation. If previous line is blank, try to find previous with code.
    prev_idx = idx - 1
    while prev_idx >= 0 and lines[prev_idx].strip() == '':
        prev_idx -= 1
    if prev_idx < 0:
        print('  Could not find previous non-empty line; skipping', f)
        continue
    prev_indent = len(lines[prev_idx]) - len(lines[prev_idx].lstrip(' '))
    cur_line = lines[idx]
    cur_indent = len(cur_line) - len(cur_line.lstrip(' '))
    print(f'  prev_indent={prev_indent} cur_indent={cur_indent}')
    if cur_indent <= prev_indent:
        print('  Current indent already <= previous; skipping auto-fix')
        continue

    # Create new line with reduced indentation to prev_indent
    new_line = ' ' * prev_indent + cur_line.lstrip(' ')
    lines[idx] = new_line

    # Write back and try compile again
    new_text = '\n'.join(lines) + '\n'
    try:
        compile(new_text, str(f), 'exec')
        f.write_text(new_text, encoding='utf-8')
        fixed_files.append(f)
        print('  Fixed', f)
    except Exception as e:
        print('  Fix failed for', f, '->', e)
        # attempt a more aggressive approach: dedent multiple successive lines if they are similarly over-indented
        # but avoid automatic aggressive edits; leave for manual review

print('\nSummary:')
print('  ui files checked:', len(ui_files))
print('  fixed files:', len(fixed_files))
for ff in fixed_files:
    print('   -', ff)
print('  files with problems (not fixed):')
for f, err in problems:
    if f not in fixed_files:
        print('   -', f, type(err).__name__, getattr(err,'msg',err))
