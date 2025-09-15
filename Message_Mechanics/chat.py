from Message_Mechanics.messages import Message
from PySide6.QtWidgets import QScrollArea,QLayout

class Chat:
    def __init__(self,widget:QScrollArea):
        self.chat_widget = widget
        self.MessagesWidgets = self.chat_widget.widget()
        self.Layout :QLayout = self.MessagesWidgets.layout() # type: ignore
        self.messages = []
    def set_target(self,target):
        self.target = target
    def add_message(self,message:Message):
        self.Layout.addWidget(message.get_widget())
        self.messages.append(message.get_dict())
        if message.get_dict()["role"] == "user":
            self.target.respond(message)