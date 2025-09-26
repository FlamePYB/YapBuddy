
from src.Utils.file_handling import get_file_content_of
from res import res_rc
import os
from PySide6.QtCore import QFile, QTextStream, QIODevice
from PySide6.QtWidgets import QWidget

def MakeCustomWidget(Loader, Target:QWidget, StyleSheet, *args):
    Loader.setupUi(Target, *args)
    try:
        # Try loading from Qt resource
        file = QFile(StyleSheet)
        if file.exists() and file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            print(f"Loaded stylesheet from Qt resource: {StyleSheet}")
            stream = QTextStream(file)
            content = stream.readAll()
            file.close()
            Target.setStyleSheet(content)
        else:
            # Fallback: try loading from filesystem
            if os.path.exists(StyleSheet):
                print(f"Loaded stylesheet from filesystem: {StyleSheet}")
                with open(StyleSheet, 'r', encoding='utf-8') as f:
                    Target.setStyleSheet(f.read())
            else:
                print(f"Stylesheet not found: {StyleSheet}")
                Target.setStyleSheet("")
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        Target.setStyleSheet("")
