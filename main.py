from functions import encrypt, decrypt
from logo import logo

print(logo)

while True:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if choice not in ("encode", "decode"):
        print("You typed something wrong!")
        continue
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    if choice == "encode":
        print(encrypt(message, shift))
    elif choice == "decode":
        print(decrypt(message, shift))

    if input("Type 'yes' if you want to go again. Otherwise type 'no':\n") == "no":
        break

