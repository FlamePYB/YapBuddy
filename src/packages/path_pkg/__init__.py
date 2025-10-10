import logging
from functools import cached_property
from pathlib import Path
from typing import Literal

from res import res_rc  # noqa: F401

lg = logging.getLogger(__name__)


class File:
    def __init__(self, path: str, type: Literal["ABSOLUTE", "RELATIVE"]):
        self._path = path
        match type:
            case "ABSOLUTE":
                self._base = ""
                lg.debug("Taken absolute path")
            case "RELATIVE":
                self._base = "."
                lg.debug("Used relative path")


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
