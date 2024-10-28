from string import ascii_letters

def caesar(original_message, shift_number, encode_or_decode):
    result = ""
    if encode_or_decode == "decode":
        shift_number *= -1
    for letter in original_message:
        if letter in ascii_letters:
            result += ascii_letters[(ascii_letters.index(letter) + shift_number) % 26]
        else:
            result += letter
    return f"Here's the {encode_or_decode}d result: {result}"
