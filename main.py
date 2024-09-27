import string
from time import sleep

letters = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    print("Caesar Cipher Encryption.\n")
    message = input("Type a message for encryption: ").lower()
    key = int(input("Enter a shift value:\n"))

    encrypted_message = ""

    for i in message:
        if i in letters:
            position = letters.find(i)
            current_position = (position + key) % 26
            new_character = letters[current_position]
            encrypted_message += new_character
        else:
            encrypted_message += i

    print("\nEncrypting your message 30%...\n")
    sleep(2)  # give an appearance of delay
    print("Stand by, almost finished 95%...\n")
    sleep(2)  # a little bit of delay too
    print("Your encrypted message is: " + encrypted_message)

def decrypt():
    print("Caesar Decryption.\n")
    message = input("Type a message for decryption: ").lower()
    key = int(input("Enter a shift value:\n"))

    decrypted_message = ""

    for c in message:
        if c in letters:
            position = letters.find(c)
            current_position = (position - key) % 26
            new_character = letters[current_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
            
    print("\nDecrypting your message 30%...\n")
    sleep(2)  # give an appearance of delay
    print("Stand by, almost finished 95%...\n")
    sleep(2)  # a little bit of delay too
    print("Your decrypted message is: " + decrypted_message)

def main():
    print("Caesar cipher...\n")
    cipher = input("Do you wish to encrypt or decrypt data (e/d)?: ").strip().lower()

    if cipher == "e":
        encrypt()
    elif cipher == "d":
        decrypt()
    else:
        print("Invalid option. Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
