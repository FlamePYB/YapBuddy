from API.AI_Model import generate_response
from terminal_mechanics.messages import displayed_message
from terminal_mechanics.messages import chat_log

user_in_app = True
while user_in_app :
    user_message = str(displayed_message("User"))
    model_message = displayed_message("Model",generate_response(user_input=user_message,instructions=f"you a helpful assistant , and here is the chat log of this current conversation: {chat_log}"))
    print(model_message)