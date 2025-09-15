f = QFile(":/stylesheets/MainWindow.qss")

import res_rc  # Registers Qt resources
from PySide6.QtCore import QFile

f = QFile(":/stylesheets/MainWindow.qss")
print("Exists?", f.exists())  # should be True
