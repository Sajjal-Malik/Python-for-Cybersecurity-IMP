# Registration Function
def register_user():
    print("*********Submit the Inputs to Register**********")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('user_credentials.txt', 'a') as file:
        file.write(f"{username}:{password}\n")
    print("User Registration was Successfull.")

# Login Function
def login_user():
    print("*********Welcome to Login View**********")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('user_credentials.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(':')
            if username == stored_username and password == stored_password:
                print("Login Successfull.")
                return
        print("Invalid username or password!")
        

def main():
    while True:
        print('Welcome to User Registration System')
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        choice = input('What would you like to do?: ')
        match choice:
            case '1':
                register_user()
            case '2':
                login_user()
            case '3':
                print("Exiting!")
                break
            case _:
                print("Invalid Choice, Please try again!")

main();