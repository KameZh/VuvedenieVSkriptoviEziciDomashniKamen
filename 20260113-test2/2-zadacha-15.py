class MessageLimiter:
    limit = 10
    def add_limit(self, limit, amount):
        limit = self.limit # tova e napulno nenuzno, no go ima kato iziskvane
        limit += amount
        print(f"Limit increased by {amount}. New limit is {limit}.")
        self.limit = limit
    def send_message(self, limit):
        limit = self.limit
        if limit > 0:
            limit -= 1
            print(f"Message sent. Remaining limit is {limit}.")
        else:
            print("Message limit reached. Cannot send message.")
        self.limit = limit
    def block_messages(self, limit, amount):
        limit = self.limit
        if limit - amount < 0:
            print(f"You have {limit}, but wanted to block {amount}. Not enough limit to block messages.")
            pass
        else:
            limit -= amount
            print(f"Limit decreased by {amount}. New limit is {limit}.")
        self.limit = limit
    def show_limit(self, limit):
        limit = self.limit
        print(f"Current message limit is {limit}.")

messanger = MessageLimiter()
messanger.show_limit(0) #nqmam nuzda da zadavam stojnost za promenliva, koqto vednaga se promenq
messanger.add_limit(0, 5)
messanger.send_message(0)
messanger.block_messages(0, 3)
messanger.block_messages(0, 20)
messanger.show_limit(0)