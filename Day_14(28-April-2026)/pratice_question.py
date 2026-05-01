class User():
    def __init__(self, name):
        self.name = name
class Message(User):
    def __init__(self, name):
        super().__init__(name)
        self.chat = []

    def send_message(self, msg):
        self.chat.append(msg)
        print(self.name, "sent message:", msg)
class ChatRoom(Message):
    def __init__(self, name):
        super().__init__(name)

    def joining(self):
        print("User:", self.name, "joined the chat room")

    def leaving(self):
        print("User:", self.name, "left the chat room")

    def chat_history(self):
        print("\nChat History:")
        print("User:", self.name)
        for items in self.chat:
            print(items)
s1 = ChatRoom("Sufiyan")
s1.joining()
s1.send_message("Hello everyone")
s1.send_message("How are you?")
s1.send_message("Let's study OOP")
s1.chat_history()
s1.leaving()