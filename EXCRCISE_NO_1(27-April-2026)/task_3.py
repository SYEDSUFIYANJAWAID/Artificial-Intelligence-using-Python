class User():
    def __init__(self, user_name, user_password="1234"):
        self.user_name = user_name
        self.__user_password = user_password

    def welcome(self):
        print("welcome", self.user_name)

class Message(User):
    def __init__(self, user_name):
        super().__init__(user_name)
        self.chat = []

    def sendingMessage(self):
        print("ask me anything")

class ChatRoom(Message):
    def __init__(self, user_name, chat_history=""):
        super().__init__(user_name)
        self.chat_history = chat_history

    def joining(self):
        print("user join the chat")

    def exit(self):
        print("user left the chat")

c1 = ChatRoom("sufiyan")
c1.joining()
c1.exit()
c1.sendingMessage()
c1.welcome()

   