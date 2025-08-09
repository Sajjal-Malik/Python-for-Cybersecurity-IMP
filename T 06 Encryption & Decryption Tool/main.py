from cryptography.fernet import Fernet

def generate_key(file_path = 'enryption_key.key'):
    key = Fernet.generate_key()
    with open(file_path, 'wb') as key_file:
        key_file.write(key)
    print(f"Encryption key File saved to:", {file_path})

def load_key(file_path = 'enryption_key.key'):
    with open(file_path, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(output_file, 'wb') as file:
        file.write(encrypted)
    print(f"File Encrypted and saved to: {output_file}")

def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(output_file, 'wb') as file:
        file.write(decrypted)
    print(f"File {input_file} Decrypted and saved to: {output_file}")

def main():
    print("Welcome to this Encryption / Decryption Tool!!!")
    while True:
        print("1.Generate an Encryption key.")
        print("2.Encrypt a file.")
        print("3.Decrypt a file.")
        print("4.Exit the program.")

        option = input("What option would you like to go with: ")

        if option == '1':
            file_path = input("Enter the file path to save the key (default: encryption_key.key): ") or 'encryption_key.key'
            generate_key(file_path)
        elif option == '2':
            input_file = input("Enter the path of the file to Encrypt: ")
            output_file = input("Enter the name of the output file: ")
            key_path = input("Enter path of the key or default will be used: ")
            try:
                key = load_key(key_path)
                encrypt_file(input_file, output_file, key)
            except Exception as e:
                print("Error while encrypting the file:", e)
        elif option == '3':
            input_file = input("Enter the path of the file to Decrypt: ")
            output_file = input("Enter the name of the output file: ")
            key_path = input("Enter path of the key or default will be used: ") or 'encryption_key.key'
            try:
                key = load_key(key_path)
                decrypt_file(input_file, output_file, key)
            except Exception as e:
                print("Error while decrypting the file:", e)
        elif option == '4':
            print("Exiting the Program!")
            break
        else:
            print("Please choose the valid Option.")


            
main()
        