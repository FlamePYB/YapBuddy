
from res import res_rc
import os
from PySide6.QtCore import QFile, QTextStream, QIODevice
from PySide6.QtWidgets import QWidget
from src.Utils.file_handling import get_file_content_of

def MakeCustomWidget(Loader, Target:QWidget, StyleSheet=None, *args):
    Loader.setupUi(Target, *args)
    try:
        # Only attempt to load stylesheet if path is not empty or None
        if not StyleSheet:
            return
        file = QFile(StyleSheet)
        if file.exists():
            if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
                print(f"Loaded stylesheet from Qt resource: {StyleSheet}")
                stream = QTextStream(file)
                content = stream.readAll()
                file.close()
                Target.setStyleSheet(content)
            else:
                print(f"Resource exists but could not be opened: {StyleSheet}")
            # If resource exists but can't be opened, do not fallback to file
        else:
            print(f"Resource not found: {StyleSheet}")
            # Do not fallback to file, do not set stylesheet
        # If StyleSheet is None or empty, skip setting
    except Exception as e:
        print(f"Error loading stylesheet: {e}")