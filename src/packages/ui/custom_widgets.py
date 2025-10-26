import logging as lg

from PySide6.QtWidgets import QWidget

from path_pkg import QResource, NormalFile


class CustomWidget:
    def __init__(self, loader, target: QWidget, stylesheet_resource: QResource | NormalFile | None):
        loader.setupUi(target)
        try:
            if stylesheet_resource:
                lg.info("Stylesheet resource found...")
                target.setStyleSheet(stylesheet_resource.content)
                lg.info("Stylesheet applied")
        except Exception as e:
            lg.info(f"Error loading stylesheet: {e}")
