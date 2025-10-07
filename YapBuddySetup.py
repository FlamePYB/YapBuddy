import sys
import os
from cx_Freeze import setup, Executable

# Make sure cx_Freeze can discover your src.packages modules (including res_rc.py)
src.packages_DIR = "C:/Users/machr/projects/YapBuddy/src.packages"
sys.path.insert(0, src.packages_DIR)

include_files = [
    ("C:/Users/machr/projects/YapBuddy/assets", "assets"),
    # no 'res' here; res_rc.py is code and will be frozen via imports
]

build_options = {
    "src.packages": [],  # add hidden imports if needed
    "excludes": ["tkinter", "unittest"],
    "include_files": include_files,
    "zip_include_packages": ["*"],  # zip all modules, including your src.packages
    "zip_exclude_packages": [],     # don't leave stdlib loose
    "optimize": 2,                  # compile to optimized .pyc
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="YapBuddy",
    version="1.0",
    description="Chatbot app",
    options={"build_exe": build_options},
    executables=[
        Executable(
            "C:/Users/machr/projects/YapBuddy/YapBuddy.py",
            base=base,
            target_name="YapBuddy.exe",
            icon="C:/Users/machr/projects/YapBuddy/res/files/favicon.ico"
        )
    ],
)
