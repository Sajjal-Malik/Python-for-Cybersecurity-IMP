class AdminrUser:
    def login(self):
        print("Admin user has logged in!")

class RegularUser:
    def login(self):
        print("Regular user has logged in!")


admin = AdminrUser()
user1 = RegularUser()

admin.login()
user1.login()