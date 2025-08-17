from UI.Compiled.Message import Ui_Rectangle
from Utils.widgets import MakeCustomWidget
from PySide6.QtWidgets import QWidget

class AbstractMessage(QWidget):
    def __init__(self,stylesheet):
        super().__init__()
        MakeCustomWidget(Ui_Rectangle(),self,stylesheet)

class UserMessage(AbstractMessage):
    def __init__(self):
        super().__init__("..\\stylesheets\\UserMessage.qss")

class Ai_Message(AbstractMessage):
    def __init__(self):
        super().__init__("..\\stylesheets\\Ai_Message.qss")