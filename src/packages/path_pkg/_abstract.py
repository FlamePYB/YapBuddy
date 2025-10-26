from abc import ABC, abstractmethod
from typing import Literal

import logging


lg = logging.getLogger(__name__)
class File(ABC):
    def __init__(self, path: str, path_type: Literal["ABSOLUTE", "RELATIVE"]):
        self._path = path
        match path_type:
            case "ABSOLUTE":
                self._base = ""
                lg.debug("Taken absolute path")
            case "RELATIVE":
                self._base = "."
                lg.debug("Used relative path")
    @property
    @abstractmethod
    def content(self) -> str :...