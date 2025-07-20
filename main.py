from API.AI_Model import generate_response
from terminal_mechanics.message_displaying import displayed_message

user_in_app = True
while user_in_app :
    user_message = displayed_message("User")
    model_message = displayed_message("Model",generate_response(user_input=user_message))
    print(model_message)