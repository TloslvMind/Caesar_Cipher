from string import ascii_letters

def caesar(original_message, shift_number, encode_or_decode):
    result = ""
    k = 1 if encode_or_decode == "encode" else -1
    for letter in original_message:
        if letter in ascii_letters:
            result += ascii_letters[(ascii_letters.index(letter) + shift_number * k) % 26]
        else:
            result += letter
    return f"Here's the encoded result: {result}"
