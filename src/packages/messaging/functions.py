from PySide6.QtWidgets import QLineEdit

from src.packages.messaging.chat import Chat
from src.packages.messaging.messages import Message


def get_sent_message(input_field: QLineEdit, chat: Chat):
    text = input_field.text()
    chat.add_message(Message("user", text))
    input_field.clear()


"""
def handle_enter():
        message_obj = get_sent_message(message_input_widget)  # type: ignore
        chat.add_message(message_obj)
"""
