# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\machr\\projects\\YapBuddy\\run.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\machr\\projects\\YapBuddy\\assets', 'assets/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\API', 'API/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\Message_Mechanics', 'Message_Mechanics/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\UI\\Compiled', 'Compiled/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\Utils', 'Utils/')],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\machr\\projects\\YapBuddy\\res\\files\\favicon.ico'],
)
