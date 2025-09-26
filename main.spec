# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec for YapBuddy

Entry point: run.py (launcher)
Console: yes (terminal shown)
Icon: res/files/favicon.ico

Includes:
 - compiled UI modules under src/UI/Compiled
 - resources under res/files (icons, qss)

Excludes:
 - .ui files under src/UI/editable (not needed at runtime)
 - .qrc file (res/res_rc.py is used)
"""

from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
import os

project_root = os.path.abspath(os.path.dirname(__file__))

# Entry script
script = os.path.join(project_root, 'run.py')

# Icon
icon_file = os.path.join(project_root, 'res', 'files', 'favicon.ico')

# Gather extra hidden imports for PySide6 (common hooks often handle this but be explicit)
hiddenimports = collect_submodules('PySide6')

# Include resource files (qss, images) from res/files
datas = []
res_files_dir = os.path.join(project_root, 'res', 'files')
if os.path.isdir(res_files_dir):
    for fname in os.listdir(res_files_dir):
        # include only runtime assets, not .qrc or .ui
        if fname.endswith('.ui') or fname.endswith('.qrc'):
            continue
        src = os.path.join(res_files_dir, fname)
        if os.path.isfile(src):
            # place them next to the exe under res/files/
            datas.append((src, os.path.join('res', 'files')))

# Also include the compiled resource python so import res_rc works
res_rc_py = os.path.join(project_root, 'res', 'res_rc.py')
if os.path.exists(res_rc_py):
    datas.append((res_rc_py, '.'))

# If your code expects the src package files as top-level modules (UI, Utils, etc.)
# ensure the src/ directory is bundled as a package. We'll add the entire src tree as data
# so runtime imports that rely on file-based imports continue to work.
def walk_src_data(src_root):
    out = []
    for root, dirs, files in os.walk(src_root):
        for f in files:
            if f.endswith('.pyc'):
                continue
            # exclude editable UI and qrc sources
            if f.endswith('.ui') or f.endswith('.qrc'):
                continue
            full = os.path.join(root, f)
            # store relative into the exe under src/
            rel_dir = os.path.relpath(root, src_root)
            out.append((full, os.path.join('src', rel_dir)))
    return out

src_dir = os.path.join(project_root, 'src')
if os.path.isdir(src_dir):
    datas.extend(walk_src_data(src_dir))


block_cipher = None

a = Analysis(
    [script],
    pathex=[project_root],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=['*.ui', '*.qrc'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Build a development-friendly single-file executable.
# - debug=True: keep extra debug info
# - upx=False: avoid UPX packing (faster builds and easier debugging)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='YapBuddy',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    icon=icon_file if os.path.exists(icon_file) else None,
)

# Note: For a one-file build PyInstaller uses the EXE object but the
# resulting artifact is produced as a single EXE if you run PyInstaller
# without a COLLECT step. The above configuration produces a one-file
# developer build when you run: `pyinstaller main.spec`.
