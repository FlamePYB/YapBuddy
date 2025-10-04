import sys
from cx_Freeze import setup, Executable

# Files and folders to include (datas in PyInstaller)
include_files = [
    ("C:/Users/machr/projects/YapBuddy/assets", "assets"),
    ("C:/Users/machr/projects/YapBuddy/res", "res"),
    ("C:/Users/machr/projects/YapBuddy/src/API", "API"),
    ("C:/Users/machr/projects/YapBuddy/src/Classes", "Classes"),
    ("C:/Users/machr/projects/YapBuddy/src/Message_Mechanics", "Message_Mechanics"),
    ("C:/Users/machr/projects/YapBuddy/src/UI/CustomWidgets.py", "CustomWidgets.py"),
    ("C:/Users/machr/projects/YapBuddy/src/UI/MainWindow.py", "MainWindow.py"),
    ("C:/Users/machr/projects/YapBuddy/src/UI/Message.py", "Message.py"),
    ("C:/Users/machr/projects/YapBuddy/src/Utils", "Utils"),
]

build_options = {
    "packages": [],        # add any hidden imports here if needed
    "excludes": ["tkinter", "unittest"],  # optional cleanup
    "include_files": include_files,
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],  # keep zipped
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="YapBuddy",
    version="1.0",
    description="Chatbot app",
    options={"build_exe": build_options},
    executables=[
        Executable(
            "C:/Users/machr/projects/YapBuddy/run.py",
            base=base,
            target_name="YapBuddy.exe",
            icon="C:/Users/machr/projects/YapBuddy/res/files/favicon.ico"
        )
    ],
)