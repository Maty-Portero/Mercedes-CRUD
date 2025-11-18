# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('db2.db', '.'), ('a.png', '.'), ('c.png', '.'), ('close.png', '.'), ('close2.png', '.'), ('down_arrow.png', '.'), ('logo.png', '.'), ('edit.png', '.'), ('eye.png', '.'), ('mercedes.png', '.'), ('perfil-de-usuario.png', '.'), ('search.png', '.')]
binaries = []
hiddenimports = ['main_login', 'main_rrhh', 'main_ceo', 'main_e_movilidad', 'main_e_movilidad_ceo', 'main_e_movilidad_ceo_db', 'main_e_movilidad_ceo_registro', 'main_compras', 'main_ventas', 'main_logistica', 'main_marketing', 'main_mantenimiento', 'main_produccion_tareas', 'main_produccion_almacen', 'db_manager', 'image_loader', 'ui_login', 'ui_rrhh', 'ui_ceo_home', 'ui_e_movilidad', 'ui_e_movilidad_ceo', 'ui_e_movilidad_ceo_db', 'ui_e_movilidad_ceo_registro', 'ui_compras', 'ui_ventas', 'ui_logistica', 'ui_marketing', 'ui_mantenimiento', 'ui_produccion', 'ui_produccion2']
tmp_ret = collect_all('PySide6')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['app_manager.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Mercedes-CRUD',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Mercedes-CRUD',
)
