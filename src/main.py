import logging
from sys import argv as exec_args

from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget

from src.packages.api.sdks.cerebras.Bot import ChatBot
from src.packages.messaging.chat import Chat
from src.packages.messaging.functions import get_sent_message
from src.packages.path_pkg.qt_file import QResource
from src.packages.ui.custom_widgets import CustomWidget
from src.packages.ui.generated.MainWindow import Ui_MainWindow

lg = logging.getLogger(__name__)


def main(argv=[]):
    """Start the Qt application. Called from the repo root.

    Args:
        argv: list or None. If None, uses sys.argv.

    """
    # Use the passed argv or fallback to exec_args
    _argv = argv if argv is not None else exec_args

    app = QApplication(_argv)
    lg.debug("Qt app initialized")
    window = QMainWindow()
    window_stylesheet = QResource("/style", "files/MainWindow.qss")
    CustomWidget(Ui_MainWindow(), window, window_stylesheet)
    window.show()
    message_area = window.findChild(QWidget, "MessageArea")
    message_input_widget: QLineEdit = window.findChild(QLineEdit, "MessageInput")  # type:ignore

    chat = Chat(message_area)  # type:ignore
    message_input_widget.returnPressed.connect(
        lambda: get_sent_message(message_input_widget, chat)
    )
    ChatBot(chat)

    return app.exec()
