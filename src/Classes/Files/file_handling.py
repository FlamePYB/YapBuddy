from PySide6.QtCore import QFile, QTextStream
from res import res_rc
import sys
from pathlib import Path
from functools import singledispatch
from typing import Literal

class File: # TODO: make this for virtual pathes and the shorten the repetitive work in other variants
    def __init__(self,path:str,type:Literal["ABSOLUTE","RELATIVE"]):
        self._path = path
        match type:
            case "ABSOLUTE":
                self._base = ""
            case "RELATIVE":
                self._base = "."
                
                
class NormalFile(File): #TODO: make this work for real files
    def __init__(self, path: str,type):
        super().__init__(path,type)
        self._path = path
        base_path = Path(self._base).resolve()
        self._full_path = (base_path / Path(self._path)).resolve()
    @property
    def content(self) -> str | None:
        try:
            return self._full_path.read_text(encoding="utf-8")
        except Exception:
            return None
class QResource(): 
    def __init__(self,prefix:str,path:str):
        self._file = QFile(f":{prefix}/{path}")
        self._prefix = prefix
        self._path = path
    @property
    def content(self):
        if not self._file.open(QFile.ReadOnly | QFile.Text ): 
            raise IOError(f"Cannot open resource: {self._path}")
        self._stream = QTextStream(self._file)
        self._content= self._stream.readAll()
        self._file.close()
        return self._content
