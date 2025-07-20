def displayed_message(sender,content=""):
    match sender:
        case "User":
            return str(input("You: "))
        case "Model":
            return f"AI: {content}"