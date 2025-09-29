from PySide6.QtCore import Qt

try:
    # QTextDocument used below
    from PySide6.QtGui import QTextDocument
except Exception:
    QTextDocument = None

