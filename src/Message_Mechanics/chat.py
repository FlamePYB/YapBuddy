from src.Message_Mechanics.messages import Message
from PySide6.QtWidgets import QScrollArea,QLayout
from PySide6.QtCore import Qt

class Chat:
    def __init__(self,widget:QScrollArea):
        self.chat_widget = widget
        self.MessagesWidgets = self.chat_widget.widget()
        self.Layout :QLayout = self.MessagesWidgets.layout() # type: ignore
        self.messages = []
    def set_target(self,target):
        self.target = target
    def add_message(self,message:Message):
        # add the widget then set its alignment to top so it doesn't expand vertically
        widget = message.get_widget()
        self.Layout.addWidget(widget)
        try:
            # Align left for AI, right for user so bubble widths and wrapping look correct
            role = getattr(widget, 'Role', None) or widget.property('Role')
            if role == 'User':
                self.Layout.setAlignment(widget, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
            else:
                self.Layout.setAlignment(widget, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        except Exception:
            pass
        self.messages.append(message.get_dict())
        if message.get_dict()["role"] == "user":
            self.target.respond(message)