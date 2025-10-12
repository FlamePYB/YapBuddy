from typing import Literal

from pydantic import BaseModel

from src.packages.ui.message import AiMessage, UserMessage

message_widgets = {"user": UserMessage, "assistant": AiMessage}


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

    def get_widget(self) -> UserMessage | AiMessage:
        global message_widgets
        return message_widgets[self.role](self.content)
