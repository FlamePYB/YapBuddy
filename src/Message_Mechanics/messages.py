from src.UI.CustomWidgets import UserMessage , Ai_Message
class Message:
    def __init__(self,role,content) -> None:
        self.role = role
        self.content = content
        match self.role: 
            case "assistant":
                self.widget = Ai_Message
            case "user":
                self.widget = UserMessage
    def get_widget(self):
        return self.widget(self.content)
    def get_dict(self):
                return {
                "role":self.role,
                "content":self.content
                    }