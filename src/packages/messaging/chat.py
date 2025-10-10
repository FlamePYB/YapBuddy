from PySide6.QtWidgets import QLayout, QScrollArea
from PySide6.QtCore import Qt
from dataclasses import asdict

import logging
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
        # create the widget and size it immediately using the scroll area's
        # viewport width
        widget = message.get_widget()
        self.Layout.addWidget(widget)
        try:
            # get available width from the scroll area viewport if possible
            avail = None
            try:
                avail = int(self.chat_widget.viewport().width())
            except Exception:
                avail = None
            if hasattr(widget, "prepare_for_display"):
                try:
                    widget.prepare_for_display(avail)
                except Exception:
                    logger.debug("")
        except Exception:
            pass
        # now add to layout so it's shown with the computed size
        # if the widget exposes an update_content_size helper it can be called by the
        # widget itself (on show/resize); avoid scheduling here to prevent layout thrash
        try:
            # Align left for AI, right for user so bubble widths and wrapping
            # look correct
            role = getattr(widget, "Role", None) or widget.property("Role")
            if role == "User":
                self.Layout.setAlignment(
                    widget, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop
                )
            else:
                self.Layout.setAlignment(
                    widget, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
                )
        except Exception as e:
            logger.debug(e)
        self.messages.append(asdict(message))
        if asdict(message)["role"] == "user":
            self.target.respond(message)
