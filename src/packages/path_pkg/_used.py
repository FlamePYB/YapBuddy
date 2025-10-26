import logging as lg
from functools import cached_property

from PySide6.QtCore import QFile, QTextStream

from path_pkg._abstract import File

from pathlib import Path
class QResource(QFile):
    def __init__(self, prefix: str, path: str):
        self._path = path
        self._file = QFile(f":{prefix}/{self._path}")
        lg.debug(f"{self._file!r} allocated")

    @cached_property
    def content(self):
        if not self._file.open(QFile.ReadOnly | QFile.Text):  # pyright: ignore[reportAttributeAccessIssue]
            raise OSError(f"Cannot open resource: {self._path}")
        try:
            self._stream = QTextStream(self._file)
        except Exception as e:
            lg.error(f"Unable to get resource text stream because of the error: {e} ")
            self._stream = None
        self._content = self._stream.readAll() if self._stream is not None else ""
        self._file.close()
        return self._content


class NormalFile(File):
    def __init__(self, path: str, type):
        super().__init__(path, type)
        base_path = Path(self._base).resolve()
        lg.debug("Base path resolved successfully")
        self._full_path = (base_path / Path(self._path)).resolve()
        lg.debug(f"Successfully retrieved full path :{self._full_path!s}")

    @cached_property
    def content(self) -> str:
        try:
            self.current_content = self._full_path.read_text(encoding="utf-8")
            lg.debug(f"Successfully read the file content of {self._full_path.name}")
            return self.current_content
        except Exception:
            lg.error(f"Was not able to read file {self._full_path.name}")
            return ""
