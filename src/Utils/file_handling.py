from PySide6.QtCore import QFile, QTextStream
from res import res_rc
import sys
from pathlib import Path

def get_resource(resource_path:str ) -> str:
    file = QFile(resource_path)
    if not file.open(QFile.ReadOnly | QFile.Text ): 
        raise IOError(f"Cannot open resource: {resource_path}")
    stream = QTextStream(file)
    content = stream.readAll()
    file.close()
    return content
def get_file_content_of(path: str, base_dir: str | Path | None = None) -> str:
    if path.startswith(":"):
        return get_resource(path)
    # allow caller to override base dir; default to cwd (where run.py is run from)
    if base_dir is None:
        if getattr(sys, 'frozen', False):
            base = Path(sys._MEIPASS)  # type: ignore
        else:
            base = Path.cwd()
    else:
        base = Path(base_dir)
    full_path = (base / path).resolve()
    return full_path.read_text(encoding="utf-8")
