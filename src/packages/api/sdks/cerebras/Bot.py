from api.sdks.cerebras.res.config import ai_client
from messaging.chat import Chat
from messaging.messages import Message
from path_pkg import NormalFile


class ChatBot:
    def __init__(self, chat: Chat):
        self.success: bool = True
        self.client = None
        self.client_error_message = None
        self.instructions = NormalFile(".....\\assets\\instructions.txt", type="RELATIVE")
        try:
            self.client = ai_client
        except Exception as e:
            # catch broad exceptions here so we don't silently fail later
            self.success = False
            self.client = None
            self.client_error_message = (
                f"Try again, an error occurred while creating AI client: {e}"
            )
        finally:
            self.chat = chat
            self.chat.set_target(self)

    @property
    def messages(self):
        return [
            {"role": "system", "content": self.instructions.content},
            *self.chat.messages,
        ]

    def respond(self):
        # If client wasn't initialized, return the captured error message
        if not self.success:
            err_text = self.client_error_message or "AI client unavailable."
            self.current_message = Message(role="assistant", content=err_text)
            self.chat.add_message(self.current_message)
            return

        # Accumulate streamed pieces into full_text
        answer = ""
        try:
            if not self.client or not hasattr(self.client, "chat"):
                raise RuntimeError("AI client unavailable or invalid")

            self.current_response = self.client.chat.completions.create(
                messages=self.messages,
                stream=False,
                model="llama-3.3-70b",
                temperature=0.8,
                max_tokens=300,
                top_p=1
            )

            answer = self.current_response.choices[0].message.content
            if not answer:
                answer = "No response received from model."

            self.current_message = Message(role="assistant", content=answer)
        except Exception as e:
            # Any error during streaming should produce an assistant message
            self.current_message = Message(
                role="assistant", content=f"Error while generating response: {e}"
            )

        self.chat.add_message(self.current_message)
