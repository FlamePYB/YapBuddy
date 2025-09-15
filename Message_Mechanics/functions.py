from Message_Mechanics.messages import Message
from PySide6.QtWidgets import QLineEdit
def get_sent_message(input_field:QLineEdit):
        # Get the text
    text = input_field.text()

    message = Message("user",text)
    # Clear the field
    input_field.clear()
    
    return message