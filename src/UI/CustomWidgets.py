from src.UI.Compiled.Message import Ui_Rectangle
from src.Utils.widgets import MakeCustomWidget
from PySide6.QtWidgets import QFrame,QWidget

class AbstractMessage(QFrame):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader = Ui_Rectangle()
        MakeCustomWidget(self.loader,self,StyleSheet=None)
        self.loader.MessageContent.setText(Text)
        

class UserMessage(AbstractMessage):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(Text,*args,**kwargs)
        self.setProperty("Role","User")
        # Set property on the inner QFrame so QSS selector matches
        if hasattr(self.loader, 'MessageContent'):
            # Find the QFrame created by Ui_Rectangle
            parent_frame = self.loader.MessageContent.parent()
            if parent_frame:
                parent_frame.setProperty("Role", "User")

class Ai_Message(AbstractMessage):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(Text,*args, **kwargs)
        self.setProperty("Role","Model")