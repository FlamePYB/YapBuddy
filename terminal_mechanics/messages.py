chat_log = []
def log_messages(added_message:str):
    global chat_log
    chat_log.append(added_message)


def displayed_message(sender,content=""):
    match sender:
        case "User":
            user_message = input("You: ")
            log_messages(f"User: {user_message}")
            return user_message
        case "Model":
            model_message = f"AI: {content}"
            log_messages(model_message)
            return model_message