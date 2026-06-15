def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

encoded = caesar_cipher("Hello World", 3)
decoded = caesar_decipher(encoded, 3)

print("Encoded:", encoded)
print("Decoded:", decoded)
