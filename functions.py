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