user_credentials = {}


# function to register a user
def register():
    print("======= Welcome to Register Page =======")
    print()
    username = input("Enter a username or type exit to leave: ")
    if username == 'exit':
        return False
    if username in user_credentials:
        print("Username Already exists, Please choose a different username.")
    else:
        password = input("Enter the password: ")
        user_credentials[username] = password
        print("Registration Successful.")


# function to login user
def login():
    print("======= Welcome to Login Page =======")
    print()

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_credentials and user_credentials[username] == password:
        print("Welcome Back!")
    else:
        print("Invalid username or password, Please try again later.")


def Authentication_System():
    while True:
        print("***** Basic Authentication System *****")
        print("""
            Type No. for Action
            1. Register
            2. Login
            3. Exit
                    """)
        
        option = input("Enter your choice: ")

        if option == '1':
            register()
        elif option == '2':
            login()
        elif option == '3':
            print("Exiting the System...")
            break
        else:
            print("Invalid choice, Please choose among the given options.")

# Run the Authentication system
Authentication_System()