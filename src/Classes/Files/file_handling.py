from PySide6.QtCore import QFile, QTextStream
from res import res_rc
import sys
from pathlib import Path
from deprecated import deprecated

class File: # TODO: make this for virtual pathes and the shorten the repetitive work in other variants
    def __init__(self,path):
        pass
class QResource(File): 
    def __init__(self,prefix,path):
        file = QFile(f":{prefix}/{path}")
        if not file.open(QFile.ReadOnly | QFile.Text ): 
            raise IOError(f"Cannot open resource: {path}")
        self._stream = QTextStream(file)
        self._content = self._stream.readAll()
        file.close()
class NormalFile(File): #TODO: make this work for real files
    pass
class FrozenFile(NormalFile): #TODO: make this work for files in an exe
    pass
    pass
class AutoDetectedFile(File): #TODO: make this choose the variant to use depending on the file type
    pass

@deprecated
def get_file_content_of(path: str, base_dir: str | Path | None = None) -> str:
    if path.startswith(":"):
        return QResource(path)
    if base_dir is None:
        if getattr(sys, 'frozen', False):
            base = Path(sys._MEIPASS)  # type: ignore
        else:
            base = Path.cwd()
    else:
        base = Path(base_dir)
    full_path = (base / path).resolve()
    return full_path.read_text(encoding="utf-8")