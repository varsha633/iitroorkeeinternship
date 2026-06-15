def reverse_word(word):
    return word[::-1]

def is_palindrome(word):
    return word == word[::-1]

print(reverse_word("python"))
print(is_palindrome("madam"))
print(is_palindrome("hello"))
