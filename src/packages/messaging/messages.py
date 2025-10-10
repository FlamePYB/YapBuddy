from src.packages.ui.message import AiMessage, UserMessage
from dataclasses import dataclass
from typing import Literal

@dataclass
class Message:
    role : Literal["user","assistant"]
    content : str


    def get_widget(self):
        match self.role:  
            case "assistant":
                return AiMessage(self.content)
            case "user":
                return UserMessage(self.content)
