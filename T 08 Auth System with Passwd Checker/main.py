def main():
    while True:
        print('Welcome to User Registration System')
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        choice = input('What would you like to do?: ')
        
        if choice == '1':
            print("Register Selected!")
        elif choice == '2':
            print("Login Selected!")
        elif choice == '3':
            print("Exiting!")
            break
        else:
            print("Invalid Choice, Please try again!")

main();