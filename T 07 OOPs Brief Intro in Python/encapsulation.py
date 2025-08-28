class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def authenticate(self, password):
        return self.__password == password
    
user1 = User('guest', 'swordfish123')
print(user1.authenticate('swordfish123'))
print(user1.authenticate('swordfish789'))
    