import logging

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QLayout, QScrollArea

from src.packages.messaging.messages import Message

logger = logging.getLogger(__name__)


class Chat:
    def __init__(self, widget: QScrollArea):
        self.chat_widget = widget
        self.MessagesWidgets = self.chat_widget.widget()
        self.Layout: QLayout = self.MessagesWidgets.layout()  # type: ignore
        self.messages = []

    def set_target(self, target):
        self.target = target

    def add_message(self, message: Message):
        """Add a message to the chat GUI."""
        widget = message.get_widget()
        try:
            avail = int(self.chat_widget.viewport().width())
        except Exception:
            avail = 480
        if hasattr(widget, "prepare_for_display"):
            widget.prepare_for_display(avail)
        self.Layout.addWidget(widget)
        # Align left for AI, right for user
        role = getattr(widget, "Role", None) or widget.property("Role")
        if role == "User":
            self.Layout.setAlignment(
                widget, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop
            )
        else:
            self.Layout.setAlignment(
                widget, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
            )

        # Store message in history
        self.messages.append(message.model_dump())

        # Force GUI update before triggering bot response
        if message.role == "user":
            QApplication.processEvents()
            # Then trigger bot response with a slight delay
            QTimer.singleShot(100, self.target.respond)

    # ...alignment logic as before
