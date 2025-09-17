import os
from openai import OpenAI
from Utils.file_handling import get_file_content_of
from API.res.Headers import ai_client
from Message_Mechanics.messages import Message
from Message_Mechanics.chat import Chat
from openai import OpenAIError
from openai import APIError

class ChatBot:
    def __init__(self,chat:Chat):
        self.success : bool = True
        try:
            self.client = ai_client
        except APIError as e:
            self.success = False
            self.client = f"Try again, an error occured with code {e.code}"
        finally:
            self.chat = chat
            self.chat.set_target(self)
    @property
    def messages(self):
        return [
            {"role": "system",
                "content": get_file_content_of(":/text/API/res/instructions.txt")},
            *self.chat.messages
        ]
    def respond(self,user_message):
        if not self.success:
            self.current_message = Message("assistant",self.client)
        else:
            self.current_response = self.client.chat.completions.create(
            messages=self.messages,
            model="openai/gpt-4o",
            temperature=0.8,
            max_tokens=100,
            top_p=1
            )
            self.current_message = Message("assistant",
                            self.current_response.choices[0].message.content)
        self.chat.add_message(self.current_message)