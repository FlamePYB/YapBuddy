from PySide6.QtCore import QFile, QTextStream
from res import res_rc


def get_resource(resource_path:str ) -> str:
    file = QFile(resource_path)
    if not file.open(QFile.ReadOnly | QFile.Text):
        raise IOError(f"Cannot open resource: {resource_path}")
    stream = QTextStream(file)
    content = stream.readAll()
    file.close()
    return content
def get_file_content_of(path: str) -> str:
    if path[0] == ":":
        return get_resource(path)
    else:
        with open(path,"r") as file:
            return file.read()
