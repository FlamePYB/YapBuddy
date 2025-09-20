from UI.Compiled.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QLineEdit
from sys import argv as exec_args
from Utils.widgets import MakeCustomWidget
from Message_Mechanics.chat import Chat
from Message_Mechanics.messages import Message
from API.Bot import ChatBot
from Message_Mechanics.functions import get_sent_message
from functools import partial
import res_rc

app = QApplication(exec_args)

window = QMainWindow()
MakeCustomWidget(Ui_MainWindow(),window,":/stylesheets/stylesheets/MainWindow.qss")
window.show()
MessageArea = window.findChild(QWidget,"MessageArea")
message_input_widget :QLineEdit = window.findChild(QLineEdit,"MessageInput") #type:ignore
def handle_enter():
    message_obj = get_sent_message(message_input_widget) # type: ignore
    chat.add_message(message_obj)

message_input_widget.returnPressed.connect(handle_enter)

chat = Chat(MessageArea) #type:ignore
BOT = ChatBot(chat)


app.exec()