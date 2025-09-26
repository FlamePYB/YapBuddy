from src.UI.Compiled.Message import Ui_Rectangle
from src.Utils.widgets import MakeCustomWidget
from PySide6.QtWidgets import QWidget

class AbstractMessage(QWidget):
    def __init__(self,stylesheet,Text,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader = Ui_Rectangle()
        MakeCustomWidget(self.loader,self,stylesheet)
        self.loader.MessageContent.setText(Text)
        

class UserMessage(AbstractMessage):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(":/style/files/UserMessage.qss",Text,*args,**kwargs)

class Ai_Message(AbstractMessage):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(":/style/files/AI_Message.qss",Text,*args, **kwargs)