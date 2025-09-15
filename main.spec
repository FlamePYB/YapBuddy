# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\API\\res', 'res/'),('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\res_rc.py','.'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\API', 'API/'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\Message_Mechanics', 'Message_Mechanics/'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\res', 'res/'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\stylesheets', 'stylesheets/'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\UI\\Compiled', 'Compiled/'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\Utils', 'Utils/'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\UI\\CustomWidgets.py', '.'), ('C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\README.md', '.')],
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
    name='main',
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
    icon=['C:\\Users\\machr\\projects\\YapBuddy\\ChatBot\\res\\images\\favicon.ico'],
)
