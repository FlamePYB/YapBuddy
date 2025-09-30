
from res import res_rc
import os
from PySide6.QtCore import QFile, QTextStream, QIODevice
from PySide6.QtWidgets import QWidget
from src.Classes.Files.file_handling import QResource

def MakeCustomWidget(loader, target:QWidget, stylesheet_resource:QResource | None):
    loader.setupUi(target)
    try:
        if stylesheet_resource:
            target.setStyleSheet(stylesheet_resource.content)
    except Exception as e:
        print(f"Error loading stylesheet: {e}")