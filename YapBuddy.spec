# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\machr\\projects\\YapBuddy\\run.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\machr\\projects\\YapBuddy\\assets', 'assets/'), ('C:\\Users\\machr\\projects\\YapBuddy\\res', 'res/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\API', 'API/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\Classes', 'Classes/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\Message_Mechanics', 'Message_Mechanics/'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\UI\\CustomWidgets.py', '.'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\UI\\MainWindow.py', '.'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\UI\\Message.py', '.'), ('C:\\Users\\machr\\projects\\YapBuddy\\src\\Utils', 'Utils/')],
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
    [],
    exclude_binaries=True,
    name='run',
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
    icon=['C:\\Users\\machr\\projects\\YapBuddy\\res\\files\\favicon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run',
)
