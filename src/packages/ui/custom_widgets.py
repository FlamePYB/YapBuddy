from PySide6.QtWidgets import QWidget
from src.packages.path_pkg.qt_file import QResource
import logging as lg


class CustomWidget:
    def __init__(self, loader, target: QWidget, stylesheet_resource: QResource | None):
        loader.setupUi(target)
        try:
            if stylesheet_resource:
                lg.info("Stylesheet resource found...")
                target.setStyleSheet(stylesheet_resource.content)
                lg.info("Stylesheet applied")
        except Exception as e:
            lg.info(f"Error loading stylesheet: {e}")
