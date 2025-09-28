from src.UI.Compiled.Message import Ui_Rectangle
from src.Utils.widgets import MakeCustomWidget
from PySide6.QtWidgets import QFrame,QWidget
from PySide6.QtCore import Qt

try:
    # QTextDocument used below
    from PySide6.QtGui import QTextDocument
except Exception:
    QTextDocument = None

class AbstractMessage(QFrame):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader = Ui_Rectangle()
        MakeCustomWidget(self.loader,self,StyleSheet=None)
        # MessageContent is a QTextBrowser now; use setPlainText to avoid HTML rendering/truncation
        try:
            widget = self.loader.MessageContent
            # set text as plain text to avoid unexpected HTML rendering
            widget.setPlainText(Text)
            # ensure internal scrollbars are disabled
            try:
                widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            except Exception:
                pass
            # try to size the text document to the widget width so we can compute needed height
            try:
                doc = widget.document()
                # set text width to viewport width if available to get correct wrapping
                vpw = widget.viewport().width()
                if vpw > 0:
                    doc.setTextWidth(vpw)
                h = int(doc.size().height()) + 8
                # set a fixed height equal to content height so the QTextBrowser won't show its own scrollbar
                widget.setFixedHeight(max(24, h))
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
        

class UserMessage(AbstractMessage):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(Text,*args,**kwargs)
        self.setProperty("Role","User")
        # Set property on the inner QFrame so QSS selector matches
        if hasattr(self.loader, 'MessageContent'):
            # Find the QFrame created by Ui_Rectangle
            parent_frame = self.loader.MessageContent.parent()
            if parent_frame:
                    parent_frame.setProperty("Role", "User")
                    # enforce a maximum width so the bubble doesn't expand full width
                    try:
                        parent_frame.setMaximumWidth(480)
                    except Exception:
                        pass

class Ai_Message(AbstractMessage):
    def __init__(self,Text,*args, **kwargs):
        super().__init__(Text,*args, **kwargs)
        self.setProperty("Role","Model")
        # Also set the property on the inner QFrame created by Ui_Rectangle so QSS selector matches
        if hasattr(self.loader, 'MessageContent'):
            parent_frame = self.loader.MessageContent.parent()
            if parent_frame:
                    parent_frame.setProperty("Role", "Model")
                    try:
                        parent_frame.setMaximumWidth(560)
                    except Exception:
                        pass