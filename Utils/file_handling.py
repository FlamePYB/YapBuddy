from PySide6.QtCore import QFile, QTextStream
import res_rc

def get_file_content_of(resource_path: str) -> str:
    file = QFile(resource_path)
    if not file.open(QFile.ReadOnly | QFile.Text):
        raise IOError(f"Cannot open resource: {resource_path}")
    stream = QTextStream(file)
    content = stream.readAll()
    file.close()
    return content
