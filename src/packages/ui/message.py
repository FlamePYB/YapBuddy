from src.packages.ui.generated.Message import Ui_Rectangle
from src.packages.ui.custom_widgets import CustomWidget
from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import QFrame, QSizePolicy, QWidget


class AbstractMessage(QFrame):
    def __init__(self, Text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader = Ui_Rectangle()
        CustomWidget(self.loader, self, None)
        # guard flags to avoid recursive resize loops
        self._updating = False
        self._pending_resize = False
        # MessageContent is a QTextBrowser now; use setPlainText to avoid HTML rendering/truncation
        try:
            widget = self.loader.MessageContent
            # set text as plain text to avoid unexpected HTML rendering
            widget.setPlainText(Text)
            # ensure internal scrollbars are hidden
            try:
                # hide the underlying QScrollBar objects if present
                v = widget.verticalScrollBar()
                h = widget.horizontalScrollBar()
                if v is not None:
                    v.hide()
                if h is not None:
                    h.hide()
            except Exception:
                pass
            # try to size the text document to the widget width so we can compute needed height
            # initial sizing attempt; final sizing happens after the widget is laid out
            try:
                doc = widget.document()
                vpw = widget.viewport().width()
                if vpw > 0:
                    doc.setTextWidth(vpw)
                h = int(doc.size().height()) + 8
                widget.setFixedHeight(max(24, h))
                # set size policy once to prefer horizontal expansion and fixed vertical height
                try:
                    widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                except Exception:
                    pass
            except Exception:
                try:
                    widget.adjustSize()
                    widget.setFixedHeight(widget.sizeHint().height())
                except Exception:
                    pass
        except Exception:
            # fallback to setText if widget differs
            try:
                self.loader.MessageContent.setText(Text)
            except Exception:
                pass

    def update_content_size(self):
        """Lightweight resize helper: set document wrapping and adjust height once.

        We intentionally keep this simple and non-recursive so the parent layout manages widths.
        """
        widget = getattr(self.loader, "MessageContent", None)
        if widget is None:
            return
        try:
            # hide internal scrollbars
            try:
                v = widget.verticalScrollBar()
                h = widget.horizontalScrollBar()
                if v is not None:
                    v.hide()
                if h is not None:
                    h.hide()
            except Exception:
                pass

            # ensure the document wraps words and compute height
            try:
                doc = widget.document()
                # prefer viewport width if available
                vpw = 0
                try:
                    vpw = int(widget.viewport().width())
                except Exception:
                    vpw = 0
                # fallback to parent width if needed
                if not vpw:
                    try:
                        p = widget.parent()
                        vpw = int(p.width()) if p is not None else 0
                    except Exception:
                        vpw = 0

                # use a modest padding and ensure minimum width so wrapping is natural
                padding = 24
                min_width = 120
                avail = max(min_width, vpw - padding) if vpw > 0 else min_width
                doc.setTextWidth(max(1, avail - 8))
                # enable word wrap option on the document
                try:
                    opt = doc.defaultTextOption()
                    opt.setWrapMode(QTextOption.WordWrap)
                    doc.setDefaultTextOption(opt)
                except Exception:
                    pass

                h = int(doc.size().height()) + 8
                # only adjust when significantly different
                try:
                    cur_h = widget.height()
                except Exception:
                    cur_h = None
                target_h = max(24, int(round(h)))
                if cur_h is None or abs((cur_h or 0) - target_h) > 2:
                    widget.setFixedHeight(target_h)
            except Exception:
                try:
                    widget.adjustSize()
                    widget.setFixedHeight(widget.sizeHint().height())
                except Exception:
                    pass
        except Exception:
            pass

    def prepare_for_display(self, avail_width: int | None = None):
        """Compute and set the widget height given an available width from the container.

        Call this BEFORE adding the widget to the layout when possible so the widget
        is sized correctly immediately on insertion.
        """
        widget = getattr(self.loader, "MessageContent", None)
        if widget is None:
            return
        try:
            # compute a reasonable available width if none given
            try:
                if avail_width is None or avail_width <= 0:
                    # prefer the parent container width
                    p = widget.parent()
                    if p is not None:
                        avail_width = int(p.width())
                if not avail_width or avail_width <= 0:
                    # fallback to a sensible default
                    avail_width = 480
            except Exception:
                avail_width = avail_width or 480

            padding = 24
            avail = max(120, int(avail_width - padding))

            # If widget is a QLabel use its sizeHint for the given width
            from PySide6.QtWidgets import QLabel

            if isinstance(widget, QLabel):
                # ensure word wrap is on
                try:
                    widget.setWordWrap(True)
                except Exception:
                    pass
                # compute the height the label would need at approx avail width
                try:
                    # temporarily set a maximum width so sizeHint calculates wrapping, but don't fix width
                    prev_max = widget.maximumWidth()
                    widget.setMaximumWidth(avail)
                    hint = widget.sizeHint()
                    widget.setFixedHeight(hint.height())
                    # restore previous maximumWidth
                    try:
                        widget.setMaximumWidth(prev_max)
                    except Exception:
                        pass
                except Exception:
                    try:
                        widget.adjustSize()
                    except Exception:
                        pass
            else:
                # fallback for QTextBrowser-like widgets: set document width and compute height
                try:
                    doc = widget.document()
                    doc.setTextWidth(max(1, avail - 8))
                    h = int(doc.size().height()) + 8
                    widget.setFixedHeight(max(24, h))
                except Exception:
                    try:
                        widget.adjustSize()
                    except Exception:
                        pass
        except Exception:
            pass


class UserMessage(AbstractMessage):
    def __init__(self, Text, *args, **kwargs):
        super().__init__(Text, *args, **kwargs)
        self.setProperty("Role", "User")
        # Set property on the inner QFrame so QSS selector matches
        if hasattr(self.loader, "MessageContent"):
            # Find the QFrame created by Ui_Rectangle
            parent_frame = self.loader.MessageContent.parent()
            if parent_frame and isinstance(parent_frame, QWidget):
                parent_frame.setProperty("Role", "User")
                # enforce a maximum width so the bubble doesn't expand full width
                try:
                    parent_frame.setMaximumWidth(480)
                except Exception:
                    pass


class Ai_Message(AbstractMessage):
    def __init__(self, Text, *args, **kwargs):
        super().__init__(Text, *args, **kwargs)
        self.setProperty("Role", "Model")
        # Also set the property on the inner QFrame created by Ui_Rectangle so QSS selector matches
        if hasattr(self.loader, "MessageContent"):
            parent_frame = self.loader.MessageContent.parent()
            if parent_frame and isinstance(parent_frame, QWidget):
                parent_frame.setProperty("Role", "Model")
                try:
                    parent_frame.setMaximumWidth(560)
                except Exception:
                    pass
