from PySide6.QtCore import QFile, QTextStream
import logging as lg
from functools import cached_property


class QResource(QFile):
    def __init__(self, prefix: str, path: str):
        self._path = path
        self._file = QFile(f":{prefix}/{self._path}")
        lg.debug(f"{repr(self._file)} allocated")

    @property
    def content(self):
        if not self._file.open(QFile.ReadOnly | QFile.Text):
            raise IOError(f"Cannot open resource: {self._path}")
        try:
            self._stream = QTextStream(self._file)
        except Exception as e:
            lg.error(f"Unable to get resource text stream because of the error: ")
            self._stream = None
        self._content = self._stream.readAll() if self._stream is not None else ""
        self._file.close()
        return self._content
