# Code to Check if User Enter Right Password or Not

# password stored in the DB or Somewhere
stored_password = "admin1234"

#user input a password
password = input("Enter your password: ")

#check if the user password matches with stored password
if password == stored_password:
    print("Access Granted | Authenticated | Status: 200")
else:
    print("Access Denied | UnAuthenticated | Status: 401")

    
