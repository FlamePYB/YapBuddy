from src.UI.Compiled.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QLineEdit
from sys import argv as exec_args
from src.Utils.widgets import MakeCustomWidget
from src.Message_Mechanics.chat import Chat
from src.Message_Mechanics.messages import Message
from src.API.Bot import ChatBot
from src.Message_Mechanics.functions import get_sent_message
from functools import partial
from res import res_rc


def main(argv=None):
    """Start the Qt application. Call this from the repo root run.py launcher.

    Args:
        argv: list or None. If None, uses sys.argv.
    """
    # Use the passed argv or fallback to exec_args
    _argv = argv if argv is not None else exec_args

    app = QApplication(_argv)

    window = QMainWindow()
    MakeCustomWidget(Ui_MainWindow(), window, ":/style/files/MainWindow.qss")
    window.show()
    MessageArea = window.findChild(QWidget, "MessageArea")
    message_input_widget: QLineEdit = window.findChild(QLineEdit, "MessageInput")  # type:ignore

    def handle_enter():
        message_obj = get_sent_message(message_input_widget)  # type: ignore
        chat.add_message(message_obj)

    message_input_widget.returnPressed.connect(handle_enter)

    chat = Chat(MessageArea)  # type:ignore
    BOT = ChatBot(chat)

    return app.exec()


if __name__ == "__main__":
    main()