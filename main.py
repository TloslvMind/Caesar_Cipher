from string import ascii_letters


def encrypt(original_message, shift_number):
    result = ""
    for letter in original_message:
        if letter in ascii_letters:
            result += ascii_letters[(ascii_letters.index(letter) + shift_number) % 26]
        else:
            result += letter
    return f"Here's the encoded result: {result}"


def decrypt(original_message, shift_number):
    result = ""
    for letter in original_message:
        if letter in ascii_letters:
            result += ascii_letters[(ascii_letters.index(letter) - shift_number) % 26]
        else:
            result += letter
    return f"Here's the decoded result: {result}"


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

