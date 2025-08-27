class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} is logged in!")
    
class Admin(User):
    def access_logs(self):
        print(f"{self.username} is accessing the logs.")

admin_user = Admin("Admin")
admin_user.access_logs()
