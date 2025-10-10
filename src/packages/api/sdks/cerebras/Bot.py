from src.packages.api.sdks.cerebras.res.Headers import ai_client
from src.packages.messaging.chat import Chat
from src.packages.messaging.messages import Message
from src.packages.path_pkg import NormalFile


class ChatBot:
    def __init__(self, chat: Chat):
        self.success: bool = True
        self.client = None
        self.client_error_message = None
        self.instructions = NormalFile("assets\\instructions.txt", type="RELATIVE")
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

    def respond(self, user_message):
        # If client wasn't initialized, return the captured error message
        if not self.success:
            err_text = self.client_error_message or "AI client unavailable."
            self.current_message = Message("assistant", err_text)
            self.chat.add_message(self.current_message)
            return

        # Accumulate streamed pieces into full_text
        full_text = ""
        try:
            if not self.client or not hasattr(self.client, "chat"):
                raise RuntimeError("AI client unavailable or invalid")

            self.current_response = self.client.chat.completions.create(
                messages=self.messages,
                stream=True,
                model="qwen-3-235b-a22b-instruct-2507",
                temperature=0.8,
                max_tokens=100,
                top_p=1,
            )

            for chunk in self.current_response:
                # chunk can be varied shapes depending on client; be defensive
                try:
                    # try common object-like access
                    choices = getattr(chunk, "choices", None)
                    if choices is None:
                        # maybe chunk is a dict
                        choices = (
                            chunk.get("choices") if isinstance(chunk, dict) else None
                        )
                    if not choices:
                        continue

                    delta = (
                        choices[0].get("delta")
                        if isinstance(choices[0], dict)
                        else getattr(choices[0], "delta", None)
                    )
                except Exception:
                    continue

                content = None
                if isinstance(delta, dict):
                    content = delta.get("content")
                else:
                    content = getattr(delta, "content", None)

                if content:
                    full_text += content

            if not full_text:
                full_text = "No response received from model."

            self.current_message = Message("assistant", full_text)
        except Exception as e:
            # Any error during streaming should produce an assistant message
            self.current_message = Message(
                "assistant", f"Error while generating response: {e}"
            )

        self.chat.add_message(self.current_message)
