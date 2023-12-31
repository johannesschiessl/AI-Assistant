def quit(user_name):
    print(f"🧠 Assistant: 👋 Goodbye, {user_name}! Have a great day!")
    exit()

def help():
    print("📚 Available commands:")
    print("     /imagine - Generate an image")
    print("     /transcribe - Transcribe an audio file")
    print("     /text-to-speech - Convert text to speech")
    print("     /quit - Exit the program")
    print("     /help - Display the list of commands")

def error():
    print("❌ Invalid command. Please try again.")

