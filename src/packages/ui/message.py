from logging import getLogger

from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import QFrame, QLabel, QSizePolicy, QWidget

from ui.custom_widgets import CustomWidget
from ui.generated.Message import Ui_Rectangle


logger = getLogger(__name__)


class AbstractMessage(QFrame):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader = Ui_Rectangle()
        CustomWidget(self.loader, self, None)
        widget = self.loader.MessageContent
        if hasattr(widget, "setPlainText"):
            widget.setPlainText(text)
        else:
            widget.setText(text)
        self._hide_scrollbars(widget)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        widget.setMinimumWidth(120)

    def _hide_scrollbars(self, widget):
        for bar_name in ("verticalScrollBar", "horizontalScrollBar"):
            bar = getattr(widget, bar_name, lambda: None)()
            if bar:
                bar.hide()

    def prepare_for_display(self, avail_width=None):
        widget = self.loader.MessageContent
        max_user_width = 480
        max_ai_width = 560
        role = self.property("Role")
        max_width = max_user_width if role == "User" else max_ai_width
        bubble_width = min(max_width, max(120, (avail_width or max_width) - 24))
        if hasattr(widget, "document"):
            doc = widget.document()
            doc.setTextWidth(bubble_width - 8)
            opt = doc.defaultTextOption()
            opt.setWrapMode(QTextOption.WordWrap)
            doc.setDefaultTextOption(opt)
            bubble_height = max(24, int(doc.size().height()) + 8)
            widget.setFixedHeight(bubble_height)
        elif isinstance(widget, QLabel):
            widget.setWordWrap(True)
            widget.setMaximumWidth(bubble_width)
            widget.setFixedHeight(widget.sizeHint().height())
            self._hide_scrollbars(widget)


class UserMessage(AbstractMessage):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.setProperty("Role", "User")
        parent_frame = self.loader.MessageContent.parent()
        if parent_frame and isinstance(parent_frame, QWidget):
            parent_frame.setProperty("Role", "User")
            parent_frame.setMaximumWidth(480)


class AiMessage(AbstractMessage):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.setProperty("Role", "Model")
        parent_frame = self.loader.MessageContent.parent()
        if parent_frame and isinstance(parent_frame, QWidget):
            parent_frame.setProperty("Role", "Model")
            parent_frame.setMaximumWidth(560)
